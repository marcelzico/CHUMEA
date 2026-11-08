from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants
from django.utils import timezone
from utilisateur.models import Doctor
from visite_probleme.models import Visite

# Create your models here.
class Hospitalisation (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    visite = models.ForeignKey(Visite, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    date_debut = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure_debut = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())
    service = models.CharField(("Service"), max_length=50, choices=constants.SERVICE)
    chambre = models.CharField(("Chambre"), max_length=50, null=True, blank=True)
    lit = models.CharField(("Lit"), max_length=10)
    
    raison = models.TextField(("Raison de l'hospitalisation"))
    equipement = models.TextField(("Liste des équipements nécessaires"), blank=True, null=True)
    
    date_fin = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure_fin = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())
    

class Sortie(UUIDPrimaryKeyModel, TimeStampedModel):
    """Sortie du patient par la voie normale, c'est à la guerison"""
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    visite = models.ForeignKey(Visite, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    note = models.TextField(("Note de sortie"))
    date = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())


class Decharge(UUIDPrimaryKeyModel, TimeStampedModel):
    """Sortie du patient par leur demande"""
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    visite = models.ForeignKey(Visite, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    note = models.TextField(("Note de décharge"))
    date = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())
    engagement = models.FileField(("Lettre de décharge signée par un responsable du patitent"))
    

class Deces (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    visite = models.ForeignKey(Visite, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    note = models.TextField(("Note"))
    diagnostic_deces = models.TextField(("Diagnostic de décès"))
    date = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())

    
    
class Transfert(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    visite = models.ForeignKey(Visite, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    
    date_debut = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    heure_debut = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())
    
    expeditaire = models.CharField(("Service qui envoie"), max_length=100, choices=constants.SERVICE)
    destinataire = models.CharField(("Service qui reçoit"), max_length=100)
    
    raison = models.TextField(("Raison du transfert"))
    
    

