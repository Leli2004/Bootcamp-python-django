# Arquivo model para trabalhar com banco de dados

from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True) #pegar data e horário do envio do form

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulário de contatos'
        ordering = ['-data']