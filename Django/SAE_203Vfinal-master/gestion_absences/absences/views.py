from django.shortcuts import render, redirect, get_object_or_404
from .models import Groupe, Etudiant, Enseignant, Cours, Absence
from .forms import GroupeForm, EtudiantForm, EnseignantForm, CoursForm, AbsenceForm
from django.template.loader import get_template
# Accueil
def index(request):
    return render(request, 'absences/index.html')

# ----- Groupe -----
def groupes(request):
    groupes = Groupe.objects.all()
    form = GroupeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('groupes')
    return render(request, 'absences/groupes.html', {'groupes': groupes, 'form': form})

# ----- Étudiant -----
def etudiants(request):
    etudiants = Etudiant.objects.all()
    form = EtudiantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('etudiants')
    return render(request, 'absences/etudiants.html', {'etudiants': etudiants, 'form': form})

# ----- Enseignant -----
def enseignants(request):
    enseignants = Enseignant.objects.all()
    form = EnseignantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enseignants')
    return render(request, 'absences/enseignants.html', {'enseignants': enseignants, 'form': form})

# ----- Cours -----
def cours(request):
    cours = Cours.objects.all()
    form = CoursForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cours')
    return render(request, 'absences/cours.html', {'cours': cours, 'form': form})

# ----- Absences -----
def absences_view(request):
    absences = Absence.objects.all()
    form = AbsenceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('absences')
    return render(request, 'absences/absences.html', {'absences': absences, 'form': form})
def detail_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    absences = Absence.objects.filter(etudiant=etudiant)
    total = absences.count()
    justifiees = absences.filter(justifie=True).count()
    non_justifiees = total - justifiees

    context = {
        'etudiant': etudiant,
        'absences': absences,
        'total': total,
        'justifiees': justifiees,
        'non_justifiees': non_justifiees,
    }
    return render(request, 'absences/detail_etudiant.html', context)
def detail_cours(request, cours_id):
    cours = get_object_or_404(Cours, pk=cours_id)
    absences = Absence.objects.filter(cours=cours)
    total_absents = absences.count()
    justifiees = absences.filter(justifie=True).count()
    non_justifiees = total_absents - justifiees

    context = {
        'cours': cours,
        'absences': absences,
        'total': total_absents,
        'justifiees': justifiees,
        'non_justifiees': non_justifiees,
    }
    return render(request, 'absences/detail_cours.html', context)
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF')
    return response

def fiche_absence_pdf(request, absence_id):
    from .models import Absence
    absence = get_object_or_404(Absence, pk=absence_id)
    return render_to_pdf('absences/fiche_pdf.html', {'absence': absence})
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Absence

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF')
    return response

def fiche_absence_pdf(request, absence_id):
    absence = get_object_or_404(Absence, pk=absence_id)
    return render_to_pdf('absences/fiche_pdf.html', {'absence': absence})
def accueil(request):
    return render(request, 'absences/accueil.html', {'page': 'accueil'})

def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'absences/modifier_etudiant.html', {'form': form})


def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('etudiants')
    return render(request, 'absences/supprimer_etudiant.html', {'etudiant': etudiant})
def modifier_groupe(request, groupe_id):
    groupe = get_object_or_404(Groupe, id=groupe_id)
    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('groupes')
    else:
        form = GroupeForm(instance=groupe)
    return render(request, 'absences/modifier_groupe.html', {'form': form})

def supprimer_groupe(request, groupe_id):
    groupe = get_object_or_404(Groupe, id=groupe_id)
    if request.method == 'POST':
        groupe.delete()
        return redirect('groupes')
    return render(request, 'absences/supprimer_groupe.html', {'groupe': groupe})
def modifier_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('enseignants')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'absences/modifier_enseignant.html', {'form': form})

def supprimer_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('enseignants')
    return render(request, 'absences/supprimer_enseignant.html', {'enseignant': enseignant})
def modifier_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'absences/modifier_cours.html', {'form': form})

def supprimer_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours')
    return render(request, 'absences/supprimer_cours.html', {'cours': cours})
def modifier_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, request.FILES, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('absences')
    else:
        form = AbsenceForm(instance=absence)
    return render(request, 'absences/modifier_absence.html', {'form': form})

def supprimer_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    if request.method == 'POST':
        absence.delete()
        return redirect('absences')
    return render(request, 'absences/supprimer_absence.html', {'absence': absence})
