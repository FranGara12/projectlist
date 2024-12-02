from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyect_list, name='proyect_list'),
    path('proyect/create/', views.proyect_create, name='proyect_create'),
    path('proyect/<int:pk>/', views.proyect_detail, name='proyect_detail'),
    path('proyect/<int:pk>/update/', views.proyect_update, name='proyect_update'),
    path('proyect/<int:pk>/delete/', views.proyect_delete, name='proyect_delete'),
]

