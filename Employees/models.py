from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator, MinValueValidator, DecimalValidator

import performance.models


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    patronymic = models.CharField('Patronymic', max_length=30)
    phone = PhoneField('Phone number')
    work_book = models.PositiveBigIntegerField('Number of the work book',
                                               validators=[RegexValidator(regex='[А-Я]{2}\\d{7}$')])
    email = models.EmailField()
    address = models.CharField('Home address', max_length=50)
    position = models.CharField('Work position', max_length=50)
    date_of_birth = models.DateField('Date of birth')
    hiring_date = models.DateField('Hiring date')
    # TODO разбить на должность и сотрудника


class Role(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    name = models.CharField('Role name', max_length=30)
    fee = models.DecimalField(
        'Fee per role',
        validators=[
            MinValueValidator(0.01),
            DecimalValidator(decimal_places=2)
        ]
    )
