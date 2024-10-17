from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
import logging
from django.contrib import messages
import datetime
# Create your models here.





class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

 #   schedule = models.CharField(max_length=200, null=True, choices=TIMESCHEDULE)

    # current_bookings = models.IntegerField(null=True)
    # total_bookings = models.IntegerField(null=True)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()

    date_1 = models.DateField(null=True, blank=True)
    date_2 = models.DateField(null=True, blank=True)
    date_3 = models.DateField(null=True, blank=True)
    date_4 = models.DateField(null=True, blank=True)

    reservation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    


class Movie(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='files/covers', default='static/noposter.png', null=True, validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(1000.00)])
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True)
    release_date = models.DateField(default=timezone.now)
    showing_until = models.DateField(default=timezone.now)

    genre = models.ManyToManyField(Genre)
    runtime = models.IntegerField(null=True, validators=[MinValueValidator(45), MaxValueValidator(300)])
    rating = models.FloatField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    cast = models.TextField(null=True)
    summary = models.TextField(null=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    trailer = models.URLField()

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return str(self.title)
    
class Showtime(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True)
    theater = models.ForeignKey(Theater, on_delete=models.SET_NULL, null=True)

    date = models.DateField(null=True)

    def default_time():
        return timezone.now().strftime('%HH:%MM')

    timeslot_1 = models.TimeField(null=True, blank=True)
    timeslot_2 = models.TimeField(null=True, blank=True)
    timeslot_3 = models.TimeField(null=True, blank=True)
    timeslot_4 = models.TimeField(null=True, blank=True)

    def __str__(self):
        date = self.date.strftime('%B %d, %Y')
        return str(f"'{self.movie.title}' at {self.theater.name} on {date}")
    


class MovieTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    paid = models.BooleanField(default=False)


    def __str__(self):
        date = self.date.strftime('%B %d, %Y')
        return str(f"'{self.movie}' for {date}")


class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email = models.CharField(max_length=300,null=True, blank=True)
    contact = models.CharField(max_length=20,null=True, blank=True)
    movie_transaction = models.ForeignKey('MovieTransaction', on_delete=models.CASCADE)

    payment_method = models.CharField(max_length=50, choices=[
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'),
    ('gcash', 'GCash')
])

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f"{self.timestamp.strftime('%m-%d-%Y | %H:%M:%S')} | '{self.movie_transaction.movie}' from user: {self.user}")

    


class TheaterReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    reserve_date = models.DateField()
    event_description = models.CharField(max_length=255, null=True, blank=True)
    expected_no_attendees = models.PositiveIntegerField()
    additional_service_requirements = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(f"{self.theater.name} for {self.user} | {self.reserve_date}")


class Payment_Theater(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email = models.CharField(max_length=300,null=True, blank=True)
    contact = models.CharField(max_length=20,null=True, blank=True)
    theater_res = models.ForeignKey(TheaterReservation, on_delete=models.CASCADE)

    payment_method = models.CharField(max_length=50, choices=[
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'),
    ('gcash', 'GCash')
])

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f"{self.timestamp.strftime('%m-%d-%Y | %H:%M:%S')} | '{self.theater_res.theater}' from user: {self.user}")



# class Seat(models.Model):
#     theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
#     row_number = models.CharField(max_length=10)
#     seat_number = models.CharField(max_length=10)

#     STATUS = (
#         ('Select', 'Selected'),
#         ('Reserved', 'Reserved'),
#         ('Available', 'Available')
#     )

#     seat_status = models.CharField(max_length=50, choices=STATUS)



class ComingSoon(models.Model):
    movie_title = models.CharField(max_length=255)
    trailer = models.URLField(null=True)
    poster = models.ImageField(upload_to='files/covers', default='static/noposter.png', null=True, validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])  

    def __str__(self):
        return self.movie_title
    
# for the import logging
logger = logging.getLogger(__name__)



class TwoPreviewPick(models.Model):
    preview = models.URLField(null=True)

    @classmethod
    def get_object_count(cls):
        return cls.objects.count()
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.get_object_count() >= 2:
                logger.warning("Attempted to create more than two instances of LimitedModel.")
                return
        super().save(*args, **kwargs)