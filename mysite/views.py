#!/usr/bin/python -tt
#!coding:utf8
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import datetime
from weibo import APIClient
###################################################
#这个方法用来区分post和get
def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return page_get(request)
    if request.method == 'POST' and POST is not None:
        return page_post(request)
#这是使用get时的方法
def page_get(request):
    assert request.method == 'GET'
    if request.GET['q']:
        query = request.GET['q']
    return render_to_response('getorpost.html',locals())
#使用post时的方法
def page_post(request):
    assert request.method == 'POST'
    if request.POST['t']:
        text = request.POST['t']
    return HttpResponseRedirect('getorpost.html',locals())
######################################################
#显示现在的时间
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())
#显示n小时以后
def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    return render_to_response('hours_ahead.html',locals())
#显示request的meta信息
def display_meta(request):
    request_path = request.get_host() + request.path
    full_path = request.get_full_path()
    is_secure = request.is_secure()
    values = request.META.items()
    values.sort()
    return render_to_response('display_meta.html', locals())
######################################################
#微博API测试
APP_KEY = '1932319785'
APP_SECRET = '57aa8eb4847fe58dc42ed24b97b39a91'
CALLBACK = 'http://localhost:8000/weibo/'
def weibo(request):
    
    if request.GET['code']:
        code = request.GET['code']
    
    return render_to_response('weibo.html',locals())
