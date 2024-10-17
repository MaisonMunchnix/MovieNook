from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupUser, name="signup"),
    path('', views.home, name='home'),
    path('movies/', views.movie, name='movie'),
    path('details/<int:pk>/', views.details, name='details'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('buy-ticket/<int:pk>', views.buyTicket, name='buyticket'),
    path('bookticket/<int:pk>', views.bookticket, name='bookticket'),
    path('book-a-theater/', views.booktheater, name='book-a-theater'),
    path('payment/<int:pk>', views.payment, name='payment'),
    path('payment-successful/<int:pk>', views.paymentsuccess, name='success'),
    path('reserve-theater/<int:pk>', views.reserveform_theater, name='reservetheater'),
    path('reservation-fee/<int:pk>', views.paymentTheater, name='pay-theater'),
    path('reservation-successful/<int:pk>', views.reservesuccess, name='reservesuccess')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)