from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

from blog import urls as blog_urls
from lifestream.rss import *
import redirects

admin.autodiscover()

urlpatterns = redirects.urlpatterns

urlpatterns += blog_urls.urlpatterns

urlpatterns += patterns('',
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/update_feeds', 'lifestream.admin_views.admin_update_feeds', name='admin_update_feeds'),
    (r'^admin/(.*)', admin.site.root),
  
    url(r'^$', 'homepage.views.main_page', name='main_page'), 
    url(r'^items/tag/(?P<tag>.+)$', 'homepage.views.tag_page', name='tag_page'),

    url(r'^$', 'homepage.views.main_page', name='lifestream_main_page'),
    url(r'^items/view/(?P<item_id>\d+)$', 'homepage.views.item_page', name='lifestream_item_page'),
    url(r'^items/site/(?P<domain>.+)$', 'homepage.views.domain_page', name='lifestream_domain_page'),

)

feeds = {
    'recent': RecentItemsFeed,
}

urlpatterns += patterns('',
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds }, name='lifestream_feeds'), 
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
