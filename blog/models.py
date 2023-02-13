from django.db import models

# Create your models here.
# post라는 class를 만들고, 속성으로 제목, 내용, 작성일, 수정일
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True) # 아예 값 자체가 지금 시간으로 자동적으로 입력됨(우리가 변경할 필요 없음)
    # created_at = models.DateTimeField(auto_now_add=True) # 값을 변경할 수는 있지만 default값으로 현재시간이 찍혀 있음
    updated_at = models.DateTimeField()
    # updated_at = models.DateTimeField(auto_now_add=True)
    # 작성자는  추후 작성 예정

    def __str__(self):
            return f'[[{self.pk}] {self.title}]'