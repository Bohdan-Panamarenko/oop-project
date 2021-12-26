from django.core.validators import RegexValidator, MinValueValidator, DecimalValidator
from django.db import models
from phone_field import PhoneField

import performance.models


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    patronymic = models.CharField('Patronymic', max_length=30)
    phone = PhoneField('Phone number')
    work_book = models.CharField('Number of the work book', max_length=9,
                                               validators=[RegexValidator(regex='[А-Я]{2}\\d{7}$')])
    email = models.EmailField('Email')
    address = models.CharField('Home address', max_length=50)
    date_of_birth = models.DateField(name='date_of_birth')

    def __str__(self):
        return self.work_book

    def get_absolute_url(self):
        return f'/employees/employees/'


class Position(models.Model):
    position = models.CharField('Work position', max_length=50)

    def get_absolute_url(self):
        return f'/employees/positions/'


class Hiring(models.Model):
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    hiring_date = models.DateField('Hiring date')

    def get_absolute_url(self):
        return f'/employees/hiring/'


class Roles(models.Model):
    performance_id = models.ForeignKey(performance.models.Performance, on_delete=models.CASCADE)
    name = models.CharField('Role name', max_length=30)

    def get_absolute_url(self):
        return f'/employees/roles_list/'


class Role(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    fee = models.DecimalField(
        'Fee per role', decimal_places=2, max_digits=20,
        validators=[
            MinValueValidator(0.01)
        ]
    )

    def get_absolute_url(self):
        return f'/employees/roles/'


class Account(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    password = models.CharField('Password', max_length=30)
    login = models.CharField('Password', max_length=30)
    photo = models.ImageField('Photo')