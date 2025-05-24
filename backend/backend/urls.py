"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.urls import path, include
from core.views import health_check

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Health check endpoint
    path('api/health/', health_check),
    
    # Redirect root to health check
    path('', lambda request: HttpResponseRedirect('/api/health/')),
    
    # Include core app URLs
    path('api/', include('core.urls')),  # Connects to core/urls.py for CRUD operations
]

