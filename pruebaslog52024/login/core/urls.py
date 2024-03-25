"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path, include
from .views import home, products, exit, creaciondeticket
from django.conf import settings
from django.conf.urls.static import static
#formulario 
from .views import register, products
#reestablecimiento de contraseña
from django.contrib.auth import views as auth_views





urlpatterns = [
   path('', home, name='home'),
   path('products/', products, name='products'),
   path('logout/', exit, name='exit'),
   path('register/', register, name='register'),
   path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('creaciondeticket/', creaciondeticket, name='creaciondeticket'),
   path('products/creaciondeticket.html', creaciondeticket, name='creaciondeticket_products'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)