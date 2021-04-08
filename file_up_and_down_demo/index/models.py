from django.db import models
from django.utils import timezone


# 文件模型
class FileModel(models.Model):
    # 文件名称
    name = models.CharField(max_length=50)

    # 文件保存路径
    path = models.CharField(max_length=100)

    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)
