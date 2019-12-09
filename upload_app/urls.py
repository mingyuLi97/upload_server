from django.urls import re_path
from upload_app import views

urlpatterns = [
    re_path(r'^$', views.upload)
]
