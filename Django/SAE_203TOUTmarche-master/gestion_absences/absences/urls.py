from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groupes/', views.groupes, name='groupes'),
    path('etudiants/', views.etudiants, name='etudiants'),
    path('enseignants/', views.enseignants, name='enseignants'),
    path('cours/', views.cours, name='cours'),
    path('absences/', views.absences_view, name='absences'),
    path('etudiant/<int:etudiant_id>/', views.detail_etudiant, name='detail_etudiant'),
    path('cours/<int:cours_id>/', views.detail_cours, name='detail_cours'),
    path('absence/<int:absence_id>/pdf/', views.fiche_absence_pdf, name='fiche_absence_pdf'),
    path('etudiant/<int:etudiant_id>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiant/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
path('groupes/modifier/<int:groupe_id>/', views.modifier_groupe, name='modifier_groupe'),
path('groupes/supprimer/<int:groupe_id>/', views.supprimer_groupe, name='supprimer_groupe'),
path('enseignant/modifier/<int:enseignant_id>/', views.modifier_enseignant, name='modifier_enseignant'),
path('enseignant/supprimer/<int:enseignant_id>/', views.supprimer_enseignant, name='supprimer_enseignant'),
path('cours/modifier/<int:cours_id>/', views.modifier_cours, name='modifier_cours'),
path('cours/supprimer/<int:cours_id>/', views.supprimer_cours, name='supprimer_cours'),
path('absences/modifier/<int:absence_id>/', views.modifier_absence, name='modifier_absence'),
path('absences/supprimer/<int:absence_id>/', views.supprimer_absence, name='supprimer_absence'),

]

