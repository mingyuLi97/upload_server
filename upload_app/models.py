from django.db import models
import datetime

# Create your models here.


class UploadImage(models.Model):
    imgName = models.CharField(max_length=256, default="", verbose_name="文件名")  # verbose_name 详细名称
    imgMd5 = models.CharField(max_length=128, verbose_name="MD5值")
    imgType = models.CharField(max_length=32, verbose_name="类型")
    imgSize = models.IntegerField(verbose_name="大小")
    imgPath = models.CharField(max_length=128, verbose_name="图片路径")
    imgCreated = models.CharField(max_length=64, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    imgUpdated = models.CharField(max_length=64, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return self.imgName

