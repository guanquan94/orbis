from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from reviews_user.views import post_list, post_create, post_detail, post_update, \
    post_delete


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^Scheduler/", include("Scheduler.urls")),
    url(r"^ratings/", include("pinax.ratings.urls")),
    url(r'^index/$', post_list, name='list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^detail/(?P<slug>[\w-]+)$', post_detail, name='detail'),
    url(r'^update/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/delete/$', post_delete), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
