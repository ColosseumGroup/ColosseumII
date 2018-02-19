from django.urls import path
from backend import views
urlpatterns = [
    path('login/',views.LoginAPI),
    path('logout/',views.LogoutAPI),
]