from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants
from django.utils import timezone
from utilisateur.models import Doctor

# Create your models here.

class Visite(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    medecin = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    
    date = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now())
    temps_debut = models.TimeField(auto_now_add=False, auto_now=False, default=timezone.now())
    
    statut = models.CharField(("Statut"), max_length=50, choices=constants.STATUT)
    
    raison = models.TextField(("Raison de la visite"))
    deroulement = models.TextField(("Déroulement de la visite"))
    conclustion = models.TextField(("Conclution"))
    
    probleme = models.BooleanField(("Est-il un problème ?"))
    
    decision = models.CharField(("Décision"), max_length=50, choices=constants.DECISION)
    


