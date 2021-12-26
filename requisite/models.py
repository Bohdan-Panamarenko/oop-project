from django.db import models

import employees.models
import performance.models
from django.core.validators import MinValueValidator


class RequisiteType(models.Model):
    type = models.CharField('Type of requisite', max_length=50)


class Requisite(models.Model):
    name = models.CharField('Name of requisite', max_length=30)
    requisite_type_id = models.ForeignKey(RequisiteType, on_delete=models.CASCADE)


class RequisiteHistory(models.Model):
    description = models.TextField('History of requisite')
    price = models.DecimalField(
        'Price of requisite', decimal_places=2, max_digits=30,
        validators=[
            MinValueValidator(0.01)
        ]
    )
    requisite_id = models.ForeignKey(Requisite, on_delete=models.CASCADE)


class RequisitePosterRole(models.Model):
    requisite_id = models.ForeignKey(Requisite, on_delete=models.CASCADE)
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    role_id = models.ForeignKey(employees.models.Role, on_delete=models.CASCADE)
