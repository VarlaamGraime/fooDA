from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('api/random-combo/', views.random_combo),
    path('api/random-combo-filtered/', views.random_combo_filtered),
]