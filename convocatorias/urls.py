from django.urls import path
#from django.urls import include
#from convocatorias.views import *
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('index.html', views.index, name='index'),
#        path('convocatorias/', views.convocatorias, name='convocatorias'),
        path('convocatorias/', views.ConvocatoriaListView.as_view(), name='convocatorias'),
        path('convocatorias/<int:pk>',views.ConvocatoriaDetailView.as_view(), name='convocatoria-detail'),
]

