from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required ##restrict pages
from .models import Movie, Theater, Showtime, ComingSoon, TwoPreviewPick, MovieTransaction, Payment, TheaterReservation, Payment_Theater
from .forms import BuyTicketForm, PaymentForm, ReserveTheaterForm, Payment_Theater_Form
# Create your views here.

# USER LOGIN AND REGISTRATION

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "")
    
    context = {'page' : page}
    return render(request, 'movienook/login_signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def signupUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during signup.')
    return render(request, 'movienook/login_signup.html', {'form':form})



# PAGES

def home(request):
    movies = Movie.objects.all()
    prev_movs = TwoPreviewPick.objects.all()
    context = {'movies' : movies, 'previews' : prev_movs}
    return render(request, 'movienook/home.html', context)


    # MOVIE PURCHASE PAGES

def movie(request):
    movies = Movie.objects.all()
    showtimes = Showtime.objects.all()
    context = {'movies' : movies, 'showtimes':showtimes}
    return render(request, 'movienook/movies.html', context)

def showtime(request):
    movies = Movie.objects.all()
    return render(request, 'movienook/showtimes.html', {'movies' : movies})


def details(request, pk):
    movie = Movie.objects.get(id=pk)
    showtime = Showtime.objects.all()
    context = {'movie' : movie, 'showtime' : showtime}
    return render(request, 'movienook/details.html', context)


def buyTicket(request, pk):
    movie = Movie.objects.get(id=pk)
    showtime = Showtime.objects.all()
    form = BuyTicketForm()
    
    if request.method == 'POST':
        form = BuyTicketForm(request.POST)
        if form.is_valid():
            ticket=form.save(commit=False)
            ticket.user = request.user
            cleaned_date = form.cleaned_data['date']
            
            ticket.save()
            
            return redirect('bookticket', pk=ticket.pk)
    else:
        form = BuyTicketForm(initial={'movie':movie})
    
    context = {'movie':movie, 'showtime':showtime, 'form':form}
    return render(request, 'movienook/buyticket_form.html', context)


def bookticket(request, pk):
    movietrans = MovieTransaction.objects.get(id=pk)
    movie = Movie.objects.all()
    total = movietrans.quantity * movietrans.movie.price
    context = {'movietrans' : movietrans, 'movie':movie,'total' :total}
            
    return render(request, 'movienook/bookticket.html', context)


def payment(request, pk):
    movie_transaction = MovieTransaction.objects.get(id=pk)
    movie = Movie.objects.all()
    total = movie_transaction.quantity * movie_transaction.movie.price

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)   
            payment.user = request.user
            payment.movie_transaction = movie_transaction
            payment.save()

            movie_transaction.paid = True
            movie_transaction.save()

            return redirect('success', pk=payment.pk)
    else:
        form = PaymentForm()

    context = {'movie_transaction': movie_transaction, 'movie' : movie, 'total':total, 'form':form}
    return render(request, 'movienook/payment_form.html', context)


def paymentsuccess(request,pk):
    payment = Payment.objects.get(id=pk)
    context = {'payment':payment}
    return render(request, 'movienook/payment_success.html', context)



    # THEATER RESERVATION


def booktheater(request):
    theaters = Theater.objects.all()
    context = {'theaters' : theaters}
    return render(request, 'movienook/booktheater.html', context)


def reserveform_theater (request, pk):
    theater = Theater.objects.get(id=pk)
    form = ReserveTheaterForm()

    if request.method == 'POST':
        form = ReserveTheaterForm(request.POST)

        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.user = request.user
            cleaned_date = form.cleaned_data['reserve_date']
            
            reserve.save()
            return redirect('pay-theater', pk=reserve.pk)
    else:
            form = ReserveTheaterForm(initial={'theater': theater})

    context = {'theater': theater, 'form' : form}
    return render (request, 'movienook/reserve_form.html', context)



def paymentTheater(request, pk):
    theater_res = TheaterReservation.objects.get(id=pk)
    
    if request.method == 'POST':
        form = Payment_Theater_Form(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)   
            reserve.user = request.user
            reserve.theater_res = theater_res
            reserve.save()

            theater_res.paid = True
            theater_res.save()

            return redirect('reservesuccess', pk=reserve.pk )
    else:
        form = Payment_Theater_Form()

    context = {'theater_res': theater_res, 'form': form}
    return render(request, 'movienook/pay_theater_form.html', context)



def reservesuccess(request,pk):
    payment = Payment_Theater.objects.get(id=pk)
    context = {'payment':payment}
    return render(request, 'movienook/reservation_successful.html', context)


# COMING SOON PAGE

def comingsoon(request):
    coming = ComingSoon.objects.all()
    context = {'coming' : coming}
    return render(request, 'movienook/comingsoon.html', context)




