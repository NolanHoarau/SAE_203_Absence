from django.db import models

class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos_etudiants/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField()
    heure = models.TimeField()
    duree = models.IntegerField(help_text="Durée en minutes")
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.date})"

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifie = models.BooleanField(default=False)
    justification = models.FileField(upload_to='justificatifs/', blank=True, null=True)

    def __str__(self):
        return f"Absence de {self.etudiant} au cours {self.cours}"
from django.db import models

class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos_etudiants/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField()
    heure = models.TimeField()
    duree = models.IntegerField(help_text="Durée en minutes")
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.date})"

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifie = models.BooleanField(default=False)
    justification = models.FileField(upload_to='justificatifs/', blank=True, null=True)

    def __str__(self):
        return f"Absence de {self.etudiant} au cours {self.cours}"
