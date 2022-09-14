from django.contrib import admin
from app.models import Game, Liga, Team


class GameAdmin(admin.ModelAdmin):
    list_display = ('liga', 'date', 'team')


class LigaAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'ghost')


admin.site.register(Game, GameAdmin)
admin.site.register(Liga, LigaAdmin)
admin.site.register(Team, TeamAdmin)
