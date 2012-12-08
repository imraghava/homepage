#:coding=utf8:

from django.conf.urls.defaults import patterns, url

from homepage.blog.feeds import (
    LatestEnglishBlogEntries,
    LatestJapaneseBlogEntries,
)

urlpatterns = patterns('django.views.generic.simple',
    # Old tag url redirect
    url(r'^(?P<locale>\w{2})/(?P<tag>[^/]+);$', 'redirect_to', {'url': '/%(locale)s/tag/%(tag)s'}, name='old_blog_tag_page'),
)

urlpatterns += patterns('homepage.blog.views',
    url(r'^admin/blog/post/(?P<object_id>[0-9]+)/preview$', 'blog_detail_preview', name='blog_detail_preview'),

    url(r'^(?P<locale>\w{2})/tag/(?P<tag>.+)$', 'tag_page', name='blog_tag_page'),
        
    url(r'^(?P<locale>\w{2})/(?P<slug>[^/]+)/?$', 'blog_detail', name='blog_detail'),
    url(r'^(?P<locale>\w{2})/?$', 'blog_page', name="blog_page"),
)

urlpatterns += patterns('',
    url(r'^feed/enfeed/$', LatestEnglishBlogEntries(), name='blog_feed_en'),
    url(r'^feed/enfeed/(?P<tag>.+)$', LatestEnglishBlogEntries(), name='blog_feed_en_tag'),
    url(r'^feed/jpfeed/$', LatestJapaneseBlogEntries(), name='blog_feed_jp'),
    url(r'^feed/jpfeed/(?P<tag>.+)$', LatestJapaneseBlogEntries(), name='blog_feed_jp_tag'),
)