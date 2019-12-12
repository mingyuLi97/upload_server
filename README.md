# upload_server
#### 服务环境

- python：3.5.2
- django：2.0

#### 开启服务

```powershell
python .\manage.py runserver
```

#### 接口

 - 描述

   > python + django 实现图片上传返回url
   >
   > 注：未添加图片验证，能够上传小于5M的文件，可以根据需求修改

- 地址

  > http://127.0.0.1:8000/upload/

- 方式

  > POST

- 请求体（body）

  - 上传格式：`multipart/form-data`
  - key: `string`
  - value: `file`

- 状态码

  - 100：失败
  - 200：成功

- 返回样例

  ```json
  {
      "urls": [
          {
              "url": "http://127.0.0.1:8000/static/images/20191212112607535.png",
              "name": "背景.png"
          },
          {
              "url": "http://127.0.0.1:8000/static/images/20191210202335345.png",
              "name": "矢量智能对象.png"
          }
      ],
      "code": 200,
      "message": "上传成功"
  }
  ```

  