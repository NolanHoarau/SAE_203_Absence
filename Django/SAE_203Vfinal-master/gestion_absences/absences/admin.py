from django.contrib import admin
from .models import Groupe, Etudiant, Enseignant, Cours, Absence

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'email', 'groupe')
    list_filter = ('groupe',)

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'email')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'date', 'heure', 'enseignant', 'groupe')
    list_filter = ('groupe', 'enseignant', 'date')

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'etudiant', 'cours', 'justifie')
    list_filter = ('justifie',)
