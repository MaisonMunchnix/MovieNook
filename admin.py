from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Theater, Showtime, ComingSoon, TwoPreviewPick, MovieTransaction, Payment, TheaterReservation, Payment_Theater

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Theater)
admin.site.register(Showtime)
admin.site.register(ComingSoon)
admin.site.register(TwoPreviewPick)
admin.site.register(MovieTransaction)
admin.site.register(Payment)
admin.site.register(TheaterReservation)
admin.site.register(Payment_Theater)