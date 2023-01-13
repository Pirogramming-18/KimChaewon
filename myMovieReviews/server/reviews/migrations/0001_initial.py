# Generated by Django 4.1.5 on 2023-01-13 02:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameMv', models.CharField(max_length=64)),
                ('yearsMv', models.DateField(help_text='개봉 년도')),
                ('genreMv', models.CharField(max_length=32)),
                ('gradeMv', models.IntegerField(help_text='0~5사이 값으로 입력하세요', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]