from rest_framework import routers
from .api import ProjectViewSet
from django.urls import path
from . import views

# Configuración del router para las rutas de la API
router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

# Definición de las URLs de la aplicación
urlpatterns = [
    path('', views.proyect_list, name='proyect_list'),
    path('proyect/create/', views.proyect_create, name='proyect_create'),
    path('proyect/<int:pk>/', views.proyect_detail, name='proyect_detail'),
    path('proyect/<int:pk>/update/', views.proyect_update, name='proyect_update'),
    path('proyect/<int:pk>/delete/', views.proyect_delete, name='proyect_delete'),
]

# Incluye las URLs de DRF (para las rutas de la API)
urlpatterns += router.urls
