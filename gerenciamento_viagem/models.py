from django.db import models

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='pacotes')
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_dias = models.IntegerField()

    def __str__(self):
        return self.nome
