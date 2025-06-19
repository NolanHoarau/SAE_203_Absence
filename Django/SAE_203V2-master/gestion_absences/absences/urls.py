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
]

