from django.contrib import admin
from .models import Sentimentos, EscalaEmocional, EstadoEmocional, Relato

admin.site.register(Sentimentos)
admin.site.register(EscalaEmocional)
admin.site.register(EstadoEmocional)
admin.site.register(Relato)
