from django.urls import path
from  . import views

urlpatterns = [
    path('signup', views.sign, name='signup'),

    path('login', views.log, name='login'),
    path('index', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('query', views.query, name='query'),
    path('search', views.search, name='search'),
    path('sell', views.sellcar, name='sellCar'),
    path('view', views.view, name='view'),
    path('cocar', views.compareCars, name='coCar'),
    path('coresult', views.compareResult, name='coResult'),

]
