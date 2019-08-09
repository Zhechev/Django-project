from django.db import models
from users.models import ProfileUser

# Create your models here.


class Object(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"
