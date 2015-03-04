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
)