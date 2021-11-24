from django.db import models

import django.core.validators as validators


class Rating(models.Model):
    description = models.TextField('Description of a rating', max_length=100)
    min_age = models.IntegerField('Minimal age of a visitor')


class Genre(models.Model):
    genre = models.TextField('Name of genre', max_length=32)


class Performance(models.Model):
    name = models.CharField('Name', max_length=64)
    rating_id = models.ForeignKey(Rating, null=True, on_delete=models.SET_NULL)
    description = models.TextField('Description of performance')
    author = models.CharField('Author', max_length=64)
    duration = models.DurationField('Duration of performance')
    genre_id = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10, validators=[
        validators.MinValueValidator(0.01)
    ])


class Hall(models.Model):
    number = models.CharField('Number of a hall', max_length=32)
    description = models.TextField('Description', max_length=100)


class Tier(models.Model):
    hall_id = models.ForeignKey(Hall, null=True, on_delete=models.CASCADE)
    level = models.IntegerField('Level of tier')
    number_of_seats = models.PositiveIntegerField('Number of seats')


class Poster(models.Model):
    performance_id = models.ForeignKey(Performance, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField('Date of performance')
    hall_id = models.ForeignKey(Hall, null=True, on_delete=models.SET_NULL)
