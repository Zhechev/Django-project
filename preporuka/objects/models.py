from django.db import models
from users.models import ProfileUser
from django.utils import timezone

# Create your models here.


class Object(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_object = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content}"