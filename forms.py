from django.forms import ModelForm
from .models import MovieTransaction,Movie, Payment, TheaterReservation, Theater, Payment_Theater
from django.forms.widgets import DateInput
from django import forms

class BuyTicketForm(ModelForm):
    class Meta:
        model = MovieTransaction
        fields = '__all__'
        exclude = ['user', 'paid']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
        

    def clean(self):
        cleaned_data = super().clean()
        valid_date = cleaned_data.get('date')
        watching_movie = cleaned_data.get('movie')

        if watching_movie:
            movie = Movie.objects.get(pk=watching_movie.pk) 
            show_until = movie.showing_until

            if valid_date > show_until:
                error_message = "Invalid date. Movie is available ONLY until {show_until}. Please choose a different date.".format(show_until=show_until)
                self.add_error('date', error_message)
                
            

        
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['user', 'movie_transaction']


class ReserveTheaterForm(ModelForm):
    class Meta:
        model = TheaterReservation
        fields = '__all__'
        exclude = ['user', 'paid']
        widgets = {
            'reserve_date' : DateInput(attrs={'type':'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        valid_date = cleaned_data.get('reserve_date')
        cinema = cleaned_data.get('theater')

        if cinema:
            theater = Theater.objects.get(pk=cinema.pk)
            dates = [theater.date_1, theater.date_2, theater.date_3, theater.date_4]

            if valid_date not in dates: 
                error_message = "WARNING: The selected date is not available for reservation. Please choose another date."
                self.add_error('reserve_date', error_message)

        return cleaned_data
    

class Payment_Theater_Form(ModelForm):
     class Meta:
        model = Payment_Theater
        fields = ['email', 'contact', 'payment_method', 'amount'] 
        