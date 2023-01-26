from django.db import models

# Create your models here.

class Dirigeant(models.Model):
    nom = models.CharField(max_length=30, unique=True)
    prenom = models.CharField(max_length=30, unique=True)

class Magasin(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=50)
    dirigeant = models.ForeignKey(Dirigeant, on_delete=models.CASCADE)
    ca = models.BigIntegerField()

class Meuble(models.Model):
    ETAT = [
        ('NF', 'NEUF'),
        ('OC','OCCASION'),
        ('ME','MAUVAIS ETAT'),
        ('')
    ]

