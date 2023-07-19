from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    