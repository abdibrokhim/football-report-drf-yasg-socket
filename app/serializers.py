from rest_framework import serializers
from app.models import Game, Liga, Team


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['liga', 'date', 'team']

    def to_representation(self, instance):
        return {
            'name': instance.liga,
            'matches': [
                {
                    'time': instance.date,
                    'team': instance.team,
                }
            ]
        }


class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = ['name', 'location', 'date']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'logo']