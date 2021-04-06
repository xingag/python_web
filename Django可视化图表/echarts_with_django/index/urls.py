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
@time: 2021/3/30 上午9:19 
@description：TODO
"""

from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name='index'),
]
