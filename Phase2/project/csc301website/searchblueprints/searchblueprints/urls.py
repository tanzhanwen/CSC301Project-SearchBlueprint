from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import home.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'searchblueprints.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^start/', 'home.views.start',
                      name='start'),
    url(r'^instruc/', 'home.views.instruc',
                      name='instruc'),
    url(r'^howitworks/', 'home.views.howitworks',
                      name='howitworks'),				  
    url(r'^compare/', 'home.views.compare',
                      name='compare'),
    
    url(r'^crawler/', 'home.views.crawler',
                      name='crawler'),
    url(r'^algorithms/','home.views.algorithms',
                      name='algorithms'),
                   
    url(r'^indexing/', 'home.views.indexing',
                      name='indexing'),
    url(r'^search/', include('haystack.urls')),
    url(r'^runScript/(?P<types>.*)', 'home.views.runScript',name='crawler2'),
    

)
