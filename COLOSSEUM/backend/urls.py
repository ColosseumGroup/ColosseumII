from django.urls import path
from backend import views
urlpatterns = [
    path('user/login/',views.LoginAPI),
    path('user/logout/',views.LogoutAPI),
    path('user/profile/',views.ProfileAPI),
    path('user/register/',views.RegisterAPI),
    path('game/create/<int:GameTypeID>/',views.CreateNewGameRoomAPI),
    path('game/list/',views.GetGameRoomListAPI),
    path('game/<int:GameID>/', views.GameInfoAPI),
    path('game/<int:GameID>/record/', views.GameStepsAPI),
]