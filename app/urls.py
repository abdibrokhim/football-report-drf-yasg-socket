from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('game-list/', views.GameList.as_view()),
    path('game-list/<int:pk>/', views.GameDetail.as_view()),
    path('liga-list/', views.LigaList.as_view()),
    path('liga-list/<int:pk>/', views.LigaDetail.as_view()),
    path('team-list/', views.TeamList.as_view()),
    path('team-list/<int:pk>/', views.TeamDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
