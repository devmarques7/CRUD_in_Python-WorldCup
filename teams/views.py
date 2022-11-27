from rest_framework.views import APIView, Request, Response
from django.forms.models import model_to_dict
from .models import Team


class TeamAssets(APIView):
    def get(self, request: Request) -> Response:
        recorde_teams = Team.objects.all()
        teams_list = []
        for team in recorde_teams:
            recorde_teams_dict = model_to_dict(team)
            teams_list.append(recorde_teams_dict)
        return Response(teams_list, 200)

    def post(self, request: Request) -> Response:
        new_team = Team.objects.create(**request.data)
        formated_dict = model_to_dict(new_team)
        return Response(formated_dict, 201)


class TeamDetails(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team_requested = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        formated_dict = model_to_dict(team_requested)
        return Response(formated_dict, 200)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team_to_update = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        for key, value in request.data.items():
            setattr(team_to_update, key, value)
        team_to_update.save()
        formated_dict = model_to_dict(team_to_update)
        return Response(formated_dict, 200)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team_to_delete = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team_to_delete.delete()
        return Response(status=204)
