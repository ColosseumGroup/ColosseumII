from django.urls import path
from backend import views
urlpatterns = [
    path('login/',views.LoginAPI),
    path('logout/',views.LogoutAPI),
    path('register/',views.RegisterAPI),
    path('game/create/<int:GameTypeID>/',views.CreateNewGameRoomAPI),
    path('game/list/',views.GetGameRoomListAPI),
    path('game/<int:GameID>/', views.GameInfoAPI),
    path('game/<int:GameID>/record/', views.GameStepsAPI),
]