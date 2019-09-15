from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # 

# Create your models here.

# model for user post's
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Authorizes user to post, on_delete erases post if user is deleted

    def __str__(self):
        return self.title
    
    