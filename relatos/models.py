from django.db import models
from django.utils import timezone
from pessoas.models import Usuario

class Sentimentos(models.Model):
    possiveis_sentimentos = [
        ("insatisfeito", "insatisfeito"),
        ("irritado", "irritado"),
        ("triste", "triste"),
        ("chateado", "chateado"),
        ("tranquilo", "tranquilo"),
        ("alegre", "alegre"),
        ("feliz", "feliz"),
        ("satisfeito", "satisfeito"),
    ]

    sentimento = models.CharField(
        max_length=12,
        choices=possiveis_sentimentos,
        default="tranquilo",
    )

class EscalaEmocional(models.Model):
    titulo = models.CharField(max_length=150, default="tranquilo")
    sentimentos = models.ManyToManyField(Sentimentos)

# Report diário não obrigatório, só emoticon referenciando sentimento
class EstadoEmocional(models.Model):
  sentimentoDeHoje = models.ForeignKey(Sentimentos, on_delete=models.CASCADE)
  criadoEm = models.DateTimeField(default=timezone.now, blank=True, null=True)
  # fk - usuario

# Report específico, com texto
class Relato(models.Model):
  estadoEmocionalNoRelato = models.ForeignKey(Sentimentos, on_delete=models.CASCADE)
  usuarioRelator = models.ForeignKey(Usuario, related_name='relato_usuario', on_delete=models.CASCADE)
  usuariosRelatados = models.ManyToManyField(Usuario, null=True)
  relato = models.TextField()
  
  # fk - usuarioRelator (relator)
  # fk - usuariosRelatados (relatados)
  # texto
  pass

