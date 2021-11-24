from django.db import models

import django.core.validators as validators


# Create your models here.


class Rating(models.Model):
    description = models.TextField()
    min_age = models.IntegerField()


class Performance(models.Model):
    name = models.CharField(max_length=64)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL)
    description = models.TextField
    author = models.CharField(max_length=64)
    duration = models.DurationField()
    genre = models.TextField(max_length=32)
    price = models.DecimalField(validators=[
        validators.MinValueValidator(0.01),
        validators.DecimalValidator(decimal_places=2)
    ])
    # TODO сделать жанр справочником


class Hall(models.Model):
    number = models.CharField(max_length=32)
    description = models.TextField()


class Tier(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    level = models.IntegerField()
    number_of_seats = models.PositiveIntegerField()


class Poster(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL)
