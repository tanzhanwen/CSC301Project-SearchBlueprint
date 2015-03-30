from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging, logging.config
from django.http import HttpResponse
import sys
import test_crawler
from django.http import HttpRequest
 
def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def start(request):
    return render_to_response('home/start.html', context_instance=RequestContext(request))

def instruc(request):
    return render_to_response('home/instruc.html', context_instance=RequestContext(request))
    
def howitworks(request):
    return render_to_response('home/howitworks.html', context_instance=RequestContext(request))

def compare(request):
    logging.info('Hello')
    return render_to_response('home/compare.html', context_instance=RequestContext(request))

def crawler(request):
    
    return render_to_response('home/crawler.html', context_instance=RequestContext(request))

def algorithms(request):
    return render_to_response('home/querying.html', context_instance=RequestContext(request))

def indexing(request):
    return render_to_response('home/indexing.html', context_instance=RequestContext(request))
def runScript(request,types):
    print(types)
    if request.method =="POST":
        a = test_crawler.testCall(types)
        print(list(a.keys()))
        return HttpResponse(a)
    else:
        return json.dumps({'message': "hello"})