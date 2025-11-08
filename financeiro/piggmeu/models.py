from django.db import models

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]

    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.descricao} ({self.get_tipo_display()})"



