from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index), # 함수
    path('', views.PostList.as_view()),  # 클래스
]