from django.db import models
from app.models import Employe, Product

act = [
    ('RM', 'Remis'),
    ('RP', 'Repris')
]

class Transfert(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    action = models.CharField(max_length=2, choices=act, default='RM')    
    date = models.DateField(auto_now_add=True)