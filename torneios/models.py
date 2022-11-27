from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

    
class Game (models.Model):
    nome_game = models.CharField(max_length=150, null=True, blank=True)
    foto_game = models.ImageField(null=True, blank=True, upload_to='static/images/torneios')
    def __str__(self):
        return self.nome_game
 
class Torneios(models.Model):
    nome_torneio = models.CharField(max_length=255)
    foto_torneio = models.ImageField(null=True, blank=True, upload_to='static/images/torneios')
    data_torneio = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.nome_torneio  

class Rodada(models.Model):
    nome_rodada = models.CharField(max_length=150, null=True, blank=True)
    data_partida = models.DateTimeField(null=True, blank=True)
    torneios = models.ForeignKey(Torneios, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_rodada
    


class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=150, null=True, blank=True)
    foto_equipe = models.ImageField(null=True, blank=True, upload_to='static/images/equipe')
    def __str__(self):
        return self.nome_equipe 
class Player(models.Model):
    nome_player = models.CharField(max_length=150, null=True, blank=True)
    foto_player = models.ImageField(null=True, blank=True, upload_to='static/images/player')
    score = models.CharField(max_length=10, null=True, blank=True)
    equipe = models.ManyToManyField(Equipe)
    def __str__(self):
        return self.nome_player
    
class Partida(models.Model):
    nome_partida = models.CharField(max_length=150, null=True, blank=True)
    data_partida = models.DateTimeField(null=True, blank=True)
    rodada = models.ManyToManyField(Rodada)
    def __str__(self):
        return self.nome_partida   
       
class Equipe1(models.Model):
    equipe1 = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    resultado = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    score = models.CharField(max_length=10, null=True, blank=True)
    class Meta:
        unique_together = ['equipe1', 'partida']
        
class Equipe2(models.Model):
    equipe2 = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    partida =models.ForeignKey(Partida, on_delete=models.CASCADE)
    resultado = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    score = models.CharField(max_length=10, null=True, blank=True)
    class Meta:
        unique_together = ['equipe2', 'partida']
    
class Situacao(models.Model):
    status = models.CharField(max_length=50)
    torneio = models.ManyToManyField(Torneios, through='TorneioSituacao', through_fields=('situacao', 'torneio'))
    def __str__(self):
        return self.status
    
class TorneioSituacao(models.Model):
    torneio = models.ForeignKey(Torneios, on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)
    class Meta:
        unique_together = ['torneio', 'situacao']
        