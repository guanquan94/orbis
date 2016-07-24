from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from reviews_user.views import post_list, post_create, post_detail, post_update, \
    post_delete, post_watch, post_unwatch, ViewWatchers, ViewOtherWatchers


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^about/', 'mysite.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("account.urls")),
    url(r'^contact/', 'contact_form.views.contact', name='contact'),
    url(r'^ratings/', include("pinax.ratings.urls")),
    url(r'^posts/$', post_list, name='list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^detail/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^edit/(?P<slug>[\w-]+)/$', post_update, name='update'),
    url(r'^delete/(?P<slug>[\w-]+)/$', post_delete), 
    
    url(r'^watch/(?P<slug>[\w-]+)/$', post_watch, name='watchlist_add'),
    url(r'^unwatch/(?P<slug>[\w-]+)/$', post_unwatch, name='watchlist_remove'),
    url(r'^watchlist/$', ViewWatchers, name='watchlist_user'),
    url(r'^watchlist/(?P<username>[\w-]+)/$', ViewOtherWatchers, name='watchlist_other_user'),
       
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^friendship/', include('friendship.urls')),
    
    #Watchlist
#     url(
#         regex=r'^(?P<content_type>[-\w]+)/(?P<obj_id>\d+)/add/$',
#         view='watchlist.views.watch',
#         name="add_to_watchlist"),
#                
#     url(
#         regex=r'^(?P<content_type>[-\w]+)/(?P<obj_id>\d+)/remove/$',
#         view='watchlist.views.unwatch',
#         name="remove_from_watchlist"),
#                
#     url(
#         regex=r'^(?P<slug>[-\w]+)/$',
#         view='watchlist.views.watchlist',
#         name="user_watchlist"),
#                
#     url(
#         regex=r'^watchlist/$',
#         name="watchlist",
#         view='watchlist.views.watchlist'),




]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
