from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.CharField(null=False, max_length=32, unique=True)
    about = models.TextField(blank=True, null=False, max_length=500)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
