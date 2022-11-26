from django.db import models


# Relacja jeden-do-jeden
class Country(models.Model):
    name = models.CharField(max_length=64)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=64)


# Relacja jeden-do-wielu
class Language(models.Model):
    name = models.CharField(max_length=64)


class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


# Relacja wiele-do-wielu
class Movie(models.Model):
    name = models.CharField(max_length=128)


class Character(models.Model):
    name = models.CharField(max_length=64)
    movies = models.ManyToManyField('Movie')
