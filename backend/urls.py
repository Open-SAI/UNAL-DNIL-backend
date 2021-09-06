"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include

from django.views.generic import RedirectView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "UNAL-DNIL Directorio Convocatorias"
admin.site.site_title = "ADMINISTRACIÓN DIRECTORIO"
admin.site.index_title = "BACKEND"

#from convocatorias.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
]

# url apps from project
urlpatterns += [
    path('', include('convocatorias.urls')),
    #path('convocatorias/', include('convocatorias.urls')),
]

#urlpatterns += [
    #path('', RedirectView.as_view(url='convocatorias/', permanent=True)),
    #path('', RedirectView.as_view(url='admin/', permanent=True)),
#]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
