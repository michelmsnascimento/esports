from django.contrib import admin
from .models import Game, Rodada, Torneios, Partida, Equipe, Equipe1, Equipe2, Player

class Equipe1Inline(admin.TabularInline):
    model = Equipe1
    extra = 1
class Equipe2Inline(admin.TabularInline):
    model = Equipe2
    extra = 1
class PartidaInline(admin.TabularInline):
    model = Partida.rodada.through
    extra = 4

class RodadaAdmin(admin.ModelAdmin):
    inlines = [
        PartidaInline
    ]

class PartidaAdmin(admin.ModelAdmin):
    inlines = [
        Equipe1Inline,
        Equipe2Inline
    ] 

class PlayerInline(admin.TabularInline):
    model = Player.equipe.through
    extra = 5
class EquipeAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline
    ]  
     
    
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Game)
admin.site.register(Torneios)
admin.site.register(Player)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Rodada, RodadaAdmin)


