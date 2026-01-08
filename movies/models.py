from django.db import models
from django.contrib.auth.models import User


#Creating models in Django means --> defining the structure of your database using Python code.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return self.name

# __str__: This is a special method in Python classes that returns a string representation of an object.
# It concatenates the movie’s id value (converted into a string) with a hyphen and the movie’s name.

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name