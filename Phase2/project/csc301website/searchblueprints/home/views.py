from django.shortcuts import render
import logging
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def start(request):
    return render_to_response('home/start.html', context_instance=RequestContext(request))

def instruc(request):
    return render_to_response('home/instruc.html', context_instance=RequestContext(request))
    
def howitworks(request):
    return render_to_response('home/howitworks.html', context_instance=RequestContext(request))

def compare(request):
    return render_to_response('home/compare.html', context_instance=RequestContext(request))

def crawler(request):
    logger.error("try",request.path)
    return render_to_response('home/crawler.html', context_instance=RequestContext(request))



def algorithms(request):
    return render_to_response('home/algorithms.html', context_instance=RequestContext(request))
