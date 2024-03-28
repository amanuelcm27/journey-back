from django.db import models
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    image = models.CharField(max_length=2000)
    description = models.TextField()
    favourite = models.BooleanField(null=True,blank=True)
    opinion = models.TextField(null=True,blank=True)
    date_finished = models.DateTimeField(auto_now_add= True)
    

class WishList(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=2000)
    date_wished = models.DateTimeField(auto_now_add = True)