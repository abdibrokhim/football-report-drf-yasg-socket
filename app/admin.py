from django.contrib import admin
from app.models import Game, Liga, Team


class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'point', 'ghost', 'team_1', 'team_2')


class LigaAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


admin.site.register(Game, GameAdmin)
admin.site.register(Liga, LigaAdmin)
admin.site.register(Team, TeamAdmin)
