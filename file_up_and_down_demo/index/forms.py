#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: forms.py 
@time: 2021/4/6 下午4:50 
@description：表单
"""
from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        # 支持多文件上传
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='请选择文件',
    )
