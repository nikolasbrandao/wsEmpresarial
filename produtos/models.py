from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.name
