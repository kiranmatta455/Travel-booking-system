
from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, UserBookingView, Bookingview

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='buslist'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name ='login'),
    path('user-bookingd/', UserBookingView.as_view(), name='user-bookings'),
    path('booking/', Bookingview.as_view(), name='bookings')

]