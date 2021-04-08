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
@time: 2021/4/6 下午3:57 
@description：TODO
"""

from django.urls import path

from .views import *

urlpatterns = [
    # 上传
    path('', index_view, name='index'),

    # 下载
    path('download/<id>', download_view, name='download')
]
