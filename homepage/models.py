from django.db import models

from django.db import models



class Category (models.Model):
    name=models.CharField(max_length=100)

class New (models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models. CASCADE)
    def __str__(self):
        return self.title