from django.http import JsonResponse
from upload_app import models
import hashlib
import os
import random
import time

# Create your views here.


def get_file_md5(file):
    md5_obj = hashlib.md5()
    for chunk in file.chunks():
        md5_obj.update(chunk)
    return md5_obj.hexdigest()


# 重命名并写入
def rename(file):
    times = time.strftime('%Y%m%d%H%M%S')
    ran = random.randint(0, 1000)
    ext = os.path.splitext(file.name)[1]
    new_file = "{}{}{}".format(times, ran, ext)
    path = os.path.join('static/images', new_file).replace('\\', '/')
    read = open(path, 'wb+')
    for chunk in file.chunks():
        read.write(chunk)
    read.close()
    return path


def upload(request):
    if request.method == 'POST':
        file = request.FILES.get('img')
        md5 = get_file_md5(file)
        img_obj = models.UploadImage.objects.filter(imgMd5=md5)
        if img_obj:
            url = "http://127.0.0.1:8000/" + img_obj.first().imgPath
            info = {'code': 200, 'url': url}
            return JsonResponse(info)
        else:
            path = rename(file)
            create = models.UploadImage.objects.create(
                imgName=os.path.basename(path),
                imgMd5=md5,
                imgType=os.path.splitext(file.name)[1],
                imgSize=file.size,
                imgPath=path)
            url = "http://127.0.0.1:8000/" + create.imgPath
            info = {'code': 200, 'url': url}
            return JsonResponse(info)


