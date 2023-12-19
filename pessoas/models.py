from django.db import models

class Usuario(models.Model):
  usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
  senhaTemporaria = models.CharField("Senha", max_length = 255, blank = False, null = True, help_text = "")
  email = models.EmailField("Email", blank = False, null = True, help_text = "", unique = True)
    