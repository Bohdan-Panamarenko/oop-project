# Generated by Django 3.2.9 on 2021-11-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_auto_20211124_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Description of a rating'),
        ),
    ]
