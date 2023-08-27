from django.urls import path
from .views import *
app_name = 'shop'

urlpatterns = [
    path('login/' , Login , name='login'),
    path("singup/",Register,name="singup"),
    path("logout/", logout_view ,name="logout"),
    path("home/",home,name="home"),
    path("ProfileUpdate/",ProfileUpdate,name='ProfileUpdate'),
    path('index/' , index , name="index"),
    path('singlepost/<slug:slug>' , singlePost , name="singlePost")


]