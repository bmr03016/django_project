from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # 작성자는  추후 작성 예정
