from django.db import models

# Create your models here.
class Genres(models.Model):
    genre_name=models.CharField(max_length=32)
    images=models.ImageField(upload_to='cat',default='sample.jpg')

class Movies(models.Model):
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    movie_duration = models.CharField(max_length=120)
    movie_poster = models.ImageField(upload_to="Posters")
    movie_file = models.FileField(upload_to="Movies")

class Cast(models.Model):
    movie_id=models.ForeignKey(Movies,on_delete=models.CASCADE)   
    castname=models.CharField(max_length=24)
    castimage=models.ImageField(upload_to='cast',)    

class Notification(models.Model):
    heading=models.CharField(max_length=56)
    message=models.TextField()   