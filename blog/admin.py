from django.contrib import admin
from .models import Post # 현재 경로의 models.py 안에 있는 Post를 가져와서 쓸 것

# Register your models here.

admin.site.register(Post)
