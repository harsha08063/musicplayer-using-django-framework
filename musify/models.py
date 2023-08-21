from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class songs(models.Model):
    song_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000,default="")
    singer=models.CharField(max_length=1000,default="")
    image=models.ImageField(upload_to="images",default="")
    songs=models.FileField(upload_to="songs",default="")
    movie=models.CharField(max_length=1000,default="")
    trending = models.BooleanField(default=False)


    def __str__(self):
        return self.name
class likedsongs(models.Model):
    liked_id=models.AutoField(primary_key=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    music_id=models.CharField(max_length=100000,default="")


