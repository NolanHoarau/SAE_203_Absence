from django.shortcuts import render, redirect, get_object_or_404
from .models import Groupe, Etudiant, Enseignant, Cours, Absence
from .forms import GroupeForm, EtudiantForm, EnseignantForm, CoursForm, AbsenceForm

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