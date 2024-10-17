# Generated by Django 5.0.4 on 2024-05-07 13:50

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import movienook.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=255)),
                ('trailer', models.URLField(null=True)),
                ('poster', models.ImageField(default='static/noposter.png', null=True, upload_to='files/covers', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(default=movienook.models.Showtime.default_time)),
                ('end_time', models.TimeField(default=movienook.models.Showtime.default_time)),
            ],
        ),
        migrations.CreateModel(
            name='TwoPreviewPicks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField()),
                ('schedules', models.ManyToManyField(to='movienook.showtime')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(default='static/noposter.png', null=True, upload_to='files/covers', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('runtime', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(45), django.core.validators.MaxValueValidator(300)])),
                ('rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('cast', models.TextField(null=True)),
                ('summary', models.TextField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('trailer', models.URLField()),
                ('genre', models.ManyToManyField(to='movienook.genre')),
                ('theater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movienook.theater')),
            ],
        ),
    ]
