from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from contas.models import Perfil
from torneios.models import Game

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
class Post(models.Model):
    autor = models.ForeignKey(Autor,  on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=255)
    game = models.ForeignKey(Game,  on_delete=models.CASCADE, null=True)
    imagem_capa = models.ImageField(null=True, blank=True, upload_to='static/news/')
    data_publicacao = models.DateTimeField(timezone.now())
    def __str__(self):
        return self.titulo

class Tag(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post) 
    def __str__(self):
        return self.nome
    
class Assunto(models.Model):
    nome = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
    
class Situacao(models.Model):
    status = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, through='PostSituacao', through_fields=('situacao', 'post'))
    def __str__(self):
        return self.status
    
class PostSituacao(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ['post', 'situacao']

class Topico(models.Model):
    conteudo = RichTextUploadingField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.conteudo
    
class Comentario(models.Model):
    texto = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.conteudo
    
    