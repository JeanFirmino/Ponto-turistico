from django.db import models

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Pontos Turisticos"

    def __str__(self):
        return self.nome