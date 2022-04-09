from django.db import models
from sqlalchemy import false

class Blog(models.Model):
    title=models.CharField(max_length=100, null=false)
    description = models.CharField(max_length=500,null=True)
    content=models.TextField()
    date =models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100, null=false)
    comment = models.CharField(max_length=500,null=false)
    date = models.DateTimeField(auto_now_add=True)
