from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField()

    def __str__(self):
            return f'[[{self.pk}] {self.title}]'