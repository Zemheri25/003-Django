
from django.urls import path
from .views import home,About

urlpatterns = [
    path('', home, name= "home"),
    path('About/', About, name= "About"),


    
]
