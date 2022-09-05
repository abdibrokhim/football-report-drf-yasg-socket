from django.db import models


class Game(models.Model):
    date = models.DateTimeField(auto_now=True)
    point = models.PositiveIntegerField(default=0)
    ghost = models.BooleanField(default=False)
    team_1 = models.CharField(max_length=254)
    team_2 = models.CharField(max_length=254)

    def __str__(self):
        return self.date


class Liga(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=254)
    logo = models.ImageField(upload_to='imgs', max_length=254)

    def __str__(self):
        return self.name
