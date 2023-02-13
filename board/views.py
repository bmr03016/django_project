# from django.shortcuts import render # FBV에서 사용하는 모듈
# from .models import Post
from django.views.generic import ListView
from .models import Post

# 1) 함수형
# def index(request):
#     posts = Post.objects.all()
# 
#     return render(
#         request,
#         'board/index.html',
#         { 'posts': posts }
#     )

# 2) 클래스형 
class PostList(ListView):
    model = Post
    template_name = 'board/post_list.html'