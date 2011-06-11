from django.conf.urls.defaults import patterns, include, url
from alive.views import *

urlpatterns = patterns('',
        url(r'^$', home_page),
        url(r'^taxon/(?P<slug>[^\d]+)/$', taxon_page, name='taxon_url'),
)
