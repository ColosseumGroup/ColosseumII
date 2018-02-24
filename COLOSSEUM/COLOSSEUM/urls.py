"""COLOSSEUM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth import login,authenticate
from django.contrib import auth
from django.http import HttpResponse
import backend.urls
# from backend.serializers import UserLoginSerializer, UserSerializer
# from backend.models import User,UserProfile
from rest_framework import routers, serializers, viewsets,permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include(backend.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',TemplateView.as_view(template_name = "index.html")),
]
