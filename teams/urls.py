from .views import TeamAssets, TeamDetails
from django.urls import path

urlpatterns = [
    path("teams/", TeamAssets.as_view()),
    path("teams/<team_id>/", TeamDetails.as_view()),
]
