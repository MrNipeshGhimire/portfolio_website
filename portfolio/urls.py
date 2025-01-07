from django.urls import path
from .views.main_view import index, contactForm

urlpatterns = [
    path('',index, name="index"),
    path('contact/',contactForm, name="contact" )
    
]
