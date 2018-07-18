from django.urls import path
from backend import views
urlpatterns = [
    path('login/',views.LoginAPI),
    path('logout/',views.LogoutAPI),
    path('register/',views.RegisterAPI),
    path('game/<int:GameID>/create-new-game-room/',views.CreateNewGameRoomAPI),
    path('game/<int:GameID>/', views.GameInfoAPI),
    path('game/<int:GameID>/record/', views.GameStepsAPI),
]