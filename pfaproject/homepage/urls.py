from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('overview/',views.general_stat, name='statistiques'),
    path('Authors/',views.authors, name='Auteurs'),
    path('Preprints/',views.preprints, name='Articles'),
    path('Authors/<int:id>/',views.auth_details, name='Auteur'),
    path('Preprints/<int:id>/',views.art_details, name='Auteur'),
]