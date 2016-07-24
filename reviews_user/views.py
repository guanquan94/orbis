from urllib import quote_plus

from account.decorators import login_required
from annoying.decorators import render_to
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post


# Create your views here.
#CRUD
@login_required
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	# if not request.user.is_authenticated():
	# 	raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
		# messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


@login_required
def post_detail(request, slug=None): #Replace Retrieve with Detail
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"has_watched": request.user in instance.watchers.all(),
	}
	return render(request, "post_detail.html", context)


@login_required
def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "abc" #You can change this anytime!
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "post_list.html", context)


@login_required
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)


@login_required
def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("list")

@login_required
def post_watch(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.watchers.add(request.user)
	messages.success(request, "Added")
	return redirect(reverse('detail', kwargs={"slug": slug}))

@login_required
def post_unwatch(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.watchers.remove(request.user)
	messages.success(request, "Removed")
	return redirect(reverse('detail', kwargs={"slug": slug}))

@login_required
@render_to('watchlist_self.html')
def ViewWatchers(request):
    return {'post_self': Post.objects.filter(watchers=request.user).order_by("title"),}
   
@login_required
@render_to('watchlist_others.html')
def ViewOtherWatchers(request, username):
    return {'post_others': Post.objects.filter(watchers__username=username).order_by("title"),
		'friendname': username}