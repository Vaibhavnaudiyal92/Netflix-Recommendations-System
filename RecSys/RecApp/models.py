from django.db import models

class Recommendations(models.Model):
    movie_name = models.CharField(max_length=100)
    'title', 'genre', 'description', 'IMDb Score', 'actors'
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name
