from django.http import JsonResponse
from upload_app import models
import hashlib
import os
import random
import time

# Create your views here.
SUCCESS_CODE = 200
SUCCESS_MESSAGE = "上传成功"

FAILURE_CODE = 100
FAILURE_MESSAGE = "上传失败"
SIZE_ERROR = "文件大小不得多于5M"


type_list = ['.png', '.jpg', '.gif', 'jpeg', '.bmp']


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
        base_url = "http://" + request.META["HTTP_HOST"] + "/"
        files = request.FILES
        if files:
            ret = {'code': SUCCESS_CODE, 'message': SUCCESS_MESSAGE, 'urls': []}
            for fileName in files:
                file = request.FILES.get(fileName)
                if file.size > 50000:
                    return JsonResponse({'code': FAILURE_CODE, 'message': SIZE_ERROR})
                md5 = get_file_md5(file)
                img_obj = models.UploadImage.objects.filter(imgMd5=md5)
                if img_obj:
                    url = base_url + img_obj.first().imgPath
                    info = {'name': file.name, 'url': url}
                else:
                    path = rename(file)
                    create = models.UploadImage.objects.create(
                        imgName=os.path.basename(path),
                        imgMd5=md5,
                        imgType=os.path.splitext(file.name)[1],
                        imgSize=file.size,
                        imgPath=path)
                    url = base_url + create.imgPath
                    info = {'name': file.name, 'url': url}
                ret['urls'].append(info)
            return JsonResponse(ret)
        else:
            return JsonResponse({'code': FAILURE_CODE, 'message': FAILURE_MESSAGE})





