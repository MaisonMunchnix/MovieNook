# Generated by Django 5.0.4 on 2024-05-09 13:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movienook', '0009_movietransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='showing_until',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
