"""
URL configuration for TP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from rest_framework import routers

from Sensor_Lister import views
from Sensor_Lister.views import CapteurViewset, CapteurDetailViewset

router = routers.SimpleRouter()
router.register('capteur-list', CapteurViewset, basename='capteur-list')
router.register('capteur-detail', CapteurDetailViewset, basename='capteur-detail')

urlpatterns = [
    path('', views.page_principale, name='page-principale'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('capteurs/', views.capteur_liste, name='capteur-liste'),
    path('capteurs/<int:id>/', views.capteur_detail, name='capteur-detail'),
    path('rechercher/', views.rechercheCapteur, name='recherche'),
    path('capteurs/ajouter/', views.capteur_ajouter, name='capteur-ajouter'),
    path('capteurs/<int:id>/modifier/', views.capteur_modifier, name='capteur-modifier'),
    path('capteurs/<int:id>/supprimer/', views.capteur_supprimer, name='capteur-supprimer'),
]
