# Create your views here.
import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.utils.http import urlquote

from .forms import *
from .models import *


def index_view(request):
    """
    上传文件
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 选择的文件
            files = request.FILES.getlist('file')

            # 遍历写入到数据库中
            for file in files:
                # 写入到数据库中
                file_model = FileModel(name=file.name, path=os.path.join('./upload', file.name))
                file_model.save()

                # 写入到服务器本地
                destination = open(os.path.join("./upload", file.name), 'wb+')
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

            # 提示上传成功
            return HttpResponse('上传成功!')
    else:
        form = FileForm()
        return render(request, 'upload.html', locals())


def download_view(request, id):
    """
    下载文件
    :param request:
    :param id:文件id
    :return:
    """
    file_result = FileModel.objects.filter(id=id)

    print(file_result)
    print(type(file_result))

    # 如果文件存在，就下载文件
    if file_result:

        file = list(file_result)[0]

        # 文件名称及路径
        name = file.name
        path = file.path

        # 读取文件
        file = open(path, 'rb')
        response = FileResponse(file)

        # 使用urlquote对文件名称进行编码
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)

        return response
    else:
        return HttpResponse('文件不存在!')
