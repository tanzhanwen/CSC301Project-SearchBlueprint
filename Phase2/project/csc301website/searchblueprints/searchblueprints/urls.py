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
    url(r'^start/', TemplateView.as_view(template_name='start.html'),
                      name='start'),
    url(r'^instruc/', TemplateView.as_view(template_name='instruc.html'),
                      name='instruc'),
    url(r'^howitworks/', TemplateView.as_view(template_name='howitworks.html'),
                      name='howitworks'),				  
    url(r'^compare/', TemplateView.as_view(template_name='compare.html'),
                      name='compare'),
    url(r'^crawler/', TemplateView.as_view(template_name='crawler.html'),
                      name='crawler'),
    url(r'^algorithms/', TemplateView.as_view(template_name='algorithms.html'),
                      name='algorithms'),
    url(r'^indexing/', TemplateView.as_view(template_name='indexing.html'),
                      name='indexing'),
    url(r'^search/', include('haystack.urls')),

)
