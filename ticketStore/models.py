from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, DecimalValidator
import performance.models
from phone_field import PhoneField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from project import settings


class Ticket(models.Model):
    price = models.DecimalField('Ticket price', decimal_places=2, max_digits=10,
                                validators=[
                                    MinValueValidator(0.01),
                                ]
                                )
    place = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    availability = models.BooleanField('Availability')
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    tier_id = models.ForeignKey(performance.models.Tier, on_delete=models.CASCADE)


class Order(models.Model):
    name = models.CharField('Name', max_length=64)
    phone = PhoneField('Phone',
                       validators=[RegexValidator(regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')])
    mail = models.CharField('Mail', max_length=64, validators=[RegexValidator(regex='[a-z0-9]+@[a-z]+\.[a-z]{2,3}')])
    date = models.DateField('Date of order')
    price = models.DecimalField('Order price', decimal_places=2, max_digits=10,
                                validators=[
                                    MinValueValidator(0.01),
                                ]
                                )
    cc_number = models.DecimalField('card number', decimal_places=0, max_digits=16,
                                    validators=[RegexValidator(regex='[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+'
                                                                     '[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]')])
    cc_expiry = models.CharField('expiration date', max_length=5,
                                 validators=[RegexValidator(regex='[0-9]+[0-9]+/[0-9]+[0-9]')])
    cc_code = models.DecimalField('security code', decimal_places=0, max_digits=3,
                                  validators=[RegexValidator(regex='[1-9]+[0-9]+[0-9]')])
    # cc_number = models.DecimalField('card number', decimal_places=0, max_digits=16,
    #                                 validators=[RegexValidator(regex='^([0-9]{16}])$')])
    # cc_expiry = models.CharField('expiration date', max_length=5,
    #                              validators=[RegexValidator(regex='^(0[1-9]|1[0-2])\/-?([0-9]{2})$')])
    # cc_code = models.DecimalField('security code', decimal_places=0, max_digits=3,
    #                               validators=[RegexValidator(regex='^([0-9]{3}])$')])


class Ticket_ordered(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField('Ticket price', decimal_places=2, max_digits=10,
                                validators=[
                                    MinValueValidator(0.01),
                                ]
                                )
    place = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    tier_id = models.IntegerField()
