from rest_framework import serializers
from app.models import Game, Liga, Team


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['date', 'point', 'ghost', 'team_1', 'team_2']


class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = ['name', 'location', 'date']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'logo']