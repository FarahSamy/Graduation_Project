from django.urls import path
from  . import views

urlpatterns = [
    path('signup', views.sign, name='signup'),

    path('login', views.log, name='login'),
    path('index', views.index, name='index'),

]
