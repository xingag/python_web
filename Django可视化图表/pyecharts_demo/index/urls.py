#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: urls.py 
@time: 2021/3/30 下午4:21 
@description：TODO
"""
from django.conf.urls import url

from index import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
