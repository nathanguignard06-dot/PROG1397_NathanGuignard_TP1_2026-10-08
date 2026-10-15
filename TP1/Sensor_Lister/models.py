from django.db import models
from django.core.validators import MinLengthValidator

class Location(models.Model):
    location_name = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.location_name}'

class Capteur(models.Model):
    class Type(models.TextChoices):
        TEMPERATURE = "T", "Température"
        HUMIDITE = "H", "Humidité"
        PRESSION = "P", "Pression"
        MOUVEMENT = "M", "Mouvement"
        GAZ = "G", "Gaz"

    nom = models.CharField(max_length=40, unique=True, validators=[MinLengthValidator(3)])
    type_capteur = models.CharField(max_length=1, choices=Type.choices)
    actif = models.BooleanField(default=True)
    detail = models.TextField(blank=True)
    emplacement = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.nom}'