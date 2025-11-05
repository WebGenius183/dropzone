from django.db import models
from slugify import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Movie')
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    length = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=1000)
    download = models.URLField()
    stream = models.URLField(blank=True)
    trailer = models.URLField(blank=True)
    trending = models.BooleanField(null=True, default=False)
    latest = models.BooleanField(default=True, auto_created=True)
    staff_pick = models.BooleanField(default=False, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating}/10)"

class Episode(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    episode = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.episode
