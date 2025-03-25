from django.db import models

# Create your models here.

from django.db import models

class CentreDeSante(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()

class Departement(models.Model):
    id_departement = models.AutoField(primary_key=True)
    centre = models.ForeignKey(CentreDeSante, on_delete=models.CASCADE)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=255)

class Receptionniste(Utilisateur):
    pass

class Medecin(Utilisateur):
    grade = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

class Patient(models.Model):
    adresse = models.TextField()
    contact = models.CharField(max_length=20)

class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_consultation = models.DateField()
    motif = models.TextField()

class HistoireMedicale(models.Model):
    id_histoire = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

class Allergie(models.Model):
    histoire_medicale = models.ForeignKey(HistoireMedicale, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)

class Vaccination(models.Model):
    histoire_medicale = models.ForeignKey(HistoireMedicale, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)

class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_examen = models.DateField()
    type_examen = models.CharField(max_length=255)

class Diagnostic(models.Model):
    id_diagnostic = models.AutoField(primary_key=True)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    date_diagnostic = models.DateField()
    resultats_diagnostics = models.TextField()

class FicheResultatExamen(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    echographie_pelvienne = models.BooleanField(default=False)
    mammographie = models.BooleanField(default=False)
    acuite_visuelle = models.BooleanField(default=False)
    pression_intraoculaire = models.BooleanField(default=False)

class Prescription(models.Model):
    id_prescription = models.AutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_prescription = models.DateField()
    cachet_prescription = models.TextField()

class FicheTraitement(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    medicaments_prescrits = models.TextField()
    interventions_chirurgicales = models.TextField()
    traitements_anterieurs = models.TextField()

class FicheEducationSante(models.Model):
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    informations_maladies_occulaires = models.TextField()
    gestion_symptomes = models.TextField()
    prevention_infections = models.TextField()
    informations_sante = models.TextField()

class FicheSuiviGrossesse(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    age_gestationnel = models.IntegerField()
    echographies_realisees = models.TextField()
    date_debut_grossesse = models.DateField()
    contexte_medical = models.TextField()
