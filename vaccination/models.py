from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants

# Create your models here.
class VaccinationPev (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    
    carnet_vaccination = models.CharField(("Carnet de vaccination"), null=True, blank=True, max_length=200)
    lieu_vaccination = models.CharField(("Lieu de vaccination"), null=True, max_length=200)
    
    premier_dose = models.BooleanField(("BCG ; VPO 0"), null=True, help_text="Age : 0 - 2 semaines")
    deuxiem_dose = models.BooleanField(("DTC 1, Hep 1, Hib 1 (Pentavalent 1) ; PCV-10 1 ; Rotarix 1 ; VPO 1"), null=True, help_text="Age : 6ème sémaine")
    troisieme_dose = models.BooleanField(("DTC 2, Hep 2, Hib 2 (Pentavalent 2) ; PCV-10 2 ; Rotarix 2 ; VPO 2"), null=True, help_text="10ème semaine")
    quatrieme_dose = models.BooleanField(("DTC 3, Hep 3, Hib 3 (Pentavalent 3) ; PCV-10 3 ; Rotarix 3 ; VPO 3"), null=True, help_text="14ème semaine")
    cinquieme_dose = models.BooleanField(("VAR 1 ; VPI 2"), null=True, help_text="9ème mois")
    sixieme_dose = models.BooleanField(("VAR 2"), null=True, help_text="15ème mois")
    
    note_vaccination = models.TextField(("Note particulière"), null=True, blank=True)
    correcte_vaccination = models.BooleanField(("Est-ce que l'enfant est correctement vacciné ?"), default=True)
    complete_vaccination = models.BooleanField(("Est-ce que l'enfant est vacciné complètement ?"))
    

class VaccinationPevHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class VaccinationAutre (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    lieu_vaccination = models.CharField(("Lieu de vaccination"), null=True, max_length=200)
    nom_vaccin = models.CharField(("Nom du vaccin"), max_length=200)
    nombre_dose = models.IntegerField(('Nombre de dose déjà reçu'))
    note_vaccination = models.TextField(("Note particulière"), null=True, blank=True)
    
    
    
    
class VaccinationAutreHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass

