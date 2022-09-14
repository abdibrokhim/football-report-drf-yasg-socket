from django.db import models


class Game(models.Model):
    liga = models.CharField(max_length=254)
    date = models.CharField(max_length=254)
    team = models.CharField(max_length=254)

    def __str__(self):
        return self.date


class Liga(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    date = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=254)
    logo = models.ImageField(upload_to='images', max_length=254)
    ghost = models.BooleanField(default=False)

    def __str__(self):
        return self.name
