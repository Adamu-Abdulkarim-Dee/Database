from django.urls import path
from . import views 

urlpatterns = [
    path('about', views.about, name='About'),
    path('terms', views.terms, name='Terms'),
    path('service', views.terms_of_service, name='Terms-Of-Service'),
    path('contact', views.Contact.as_view(), name='Contact'),
    path('BoardEdit/<slug:slug>/', views.Board.as_view(), name='Board'),
    path('login', views.login, name='Login'),
    path('new_user_register', views.register, name='Register-user')
]