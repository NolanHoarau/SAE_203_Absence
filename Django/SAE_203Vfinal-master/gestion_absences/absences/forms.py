from django import forms
from .models import Groupe, Etudiant, Enseignant, Cours, Absence

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = '__all__'

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'



class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = '__all__'
