"""
URL configuration for tuttigol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from gols import views
from django.conf.urls.static import static
from django.conf import settings
from compilations import views as compilationsViews

app_name = 'compilations'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gols/', include('gols.urls')),
    path('cerca_gol/', views.ricerca_gol, name='ricerca_gol'),
    path('visualizza_gol/<str:nomeGiocatore>/', views.ricerca_gol, name='visualizza_gol'),
    path('home/',compilationsViews.compilations_ricerca_gol, name='home'),
    path('<int:pk>/', compilationsViews.compilation_detail, name='compilation_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
