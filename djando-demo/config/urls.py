#config/urls.py (reemplaza todo el archivo)
from django.contrib import admin
from django.urls import path
from academia import views

urlpatterns = [
 path('admin/', admin.site.urls),
 path('saludo/<str:nombre>/', views.saludo),
 path('sumar/', views.sumar),
]