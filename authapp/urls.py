from django.urls import path
from .views import Home, login, signup, rooms, deluxe, family, luxury, booking, privacy, faq, terms, cancel

urlpatterns = [
    path('', Home, name='Home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
     path('rooms/', rooms, name='rooms'),
    path('deluxe/', deluxe, name='deluxe'),
    path('family/', family, name='family'),
    path('Luxury/', luxury, name='luxury'),
    path('booking/', booking, name='booking'),
    path('privacy/', privacy, name='privacy'),
    path('faq/', faq, name='faq'),
    path('terms/', terms, name='terms'),
    path('cancel/', cancel, name='cancel'),
]