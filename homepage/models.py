from django.db import models

from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title