from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField()

    def __str__(self):
        return self.name
