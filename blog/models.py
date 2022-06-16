from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    likes = models.ManyToManyField(User, related_name='blog_like')
    
    
    def __str__(self):
        return f"id: {self.id},title: {self.title},writer: {self.writer}, likes: {self.likes}"
        