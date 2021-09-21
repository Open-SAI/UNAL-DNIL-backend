from django.urls import path
from django.urls import include
#from convocatorias.views import *
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('index.html', views.index, name='index'),
#        path('convocatorias/', views.convocatorias, name='convocatorias'),
#        path('convocatorias/', views.ConvocatoriaListView.as_view(), name='convocatorias'),
        path('convocatorias/<int:pk>',views.ConvocatoriaDetailView.as_view(), name='convocatoria-detail'),
        #path('convocatorias/', views.ConvocatoriaListView.as_view(), name='convocatorias'),
        path('convocatorias/', views.SearchResultsListView.as_view(), name='convocatorias'),
        path('convocatorias/filtrar/', views.SearchResultsListView.as_view(), name='convocatorias-search'),
#        path('faicon/', include('faicon.urls')),
        path('convocatorias/enviar/', views.ConvocatoriaCreate.as_view(), name='convocatoria-create'),
]
