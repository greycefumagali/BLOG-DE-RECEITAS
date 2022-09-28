from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(default='')
    conteudo = models.TextField(default='')
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    postado_em = models.DateField(auto_now_add=True)
    mostrar = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem = models.TextField(default='')

    def __str__(self):
        return self.titulo
