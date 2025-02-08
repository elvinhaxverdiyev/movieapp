from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=100, blank=True, null=True)
    actors = models.CharField(max_length=255, blank=True, null=True)
    genre = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='movieapp/', blank=True, null=True)
    link =  models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.movie.title}"
    
    

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.email