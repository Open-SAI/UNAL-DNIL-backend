from django.urls import path
#from django.urls import include
#from convocatorias.views import *
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('index.html', views.index, name='index'),
        path('convocatorias/', views.convocatorias, name='convocatorias'),
]

