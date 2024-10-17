# Generated by Django 5.0.4 on 2024-05-12 00:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movienook', '0016_alter_movie_options_movietransaction_paid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TheaterReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateField()),
                ('event_description', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_no_attendees', models.PositiveIntegerField()),
                ('additional_service_requirements', models.CharField(blank=True, max_length=255, null=True)),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienook.theater')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
