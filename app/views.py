from app.models import Game, Liga, Team
from app.serializers import GameSerializer, LigaSerializer, TeamSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GameList(APIView):
    def get(self, request,):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request,):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetail(APIView):
    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk,):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk,):
        game = self.get_object(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LigaList(APIView):
    def get(self, request,):
        ligas = Liga.objects.all()
        serializer = LigaSerializer(ligas, many=True)
        return Response(serializer.data)

    def post(self, request,):
        serializer = LigaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LigaDetail(APIView):
    def get_object(self, pk):
        try:
            return Liga.objects.get(pk=pk)
        except Liga.DoesNotExist:
            raise Http404

    def get(self, request, pk,):
        liga = self.get_object(pk)
        serializer = LigaSerializer(liga)
        return Response(serializer.data)

    def put(self, request, pk,):
        liga = self.get_object(pk)
        serializer = LigaSerializer(liga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,):
        liga = self.get_object(pk)
        liga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamList(APIView):
    def get(self, request,):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request,):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk,):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk,):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)