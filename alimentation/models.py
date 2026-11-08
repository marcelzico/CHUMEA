from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants
# Create your models here.
class Alimentation (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    ame = models.BooleanField(("Allaitement maternel exclusive"), default=True)
    diversification_debut = models.CharField(("Début de la diversification allimentaire (fin de l'AME aussi)"), max_length=50)
    diversification_aliment = models.TextField(("Aliment(s) de diversification"), blank=True, null=True)
    sevrage_temps = models.CharField(("Sevrage du lait maternel (si applicable)"), max_length=100, blank=True, null=True)
    regime_actuelle = models.CharField(("Régime actuel"), max_length=200, blank=True, null=True)
    note_alimentaion = models.TextField(("Note particulière concernant l'alimentation"), blank=True, null=True)
    conclusion = models.CharField(("Conclusion"), max_length=100, choices=constants.ALIMENTATION_CONCLUSION, default="normocalorique")
    

class AlimentationHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    alimentation = models.ForeignKey(Alimentation, on_delete=models.CASCADE, related_name='historique')
    ame = models.BooleanField(("Allaitement maternel exclusive"), default=True)
    diversification_debut = models.CharField(("Début de la diversification allimentaire (fin de l'AME aussi)"), max_length=50)
    diversification_aliment = models.TextField(("Aliment(s) de diversification"), blank=True, null=True)
    sevrage_temps = models.CharField(("Sevrage du lait maternel (si applicable)"), max_length=100, blank=True, null=True)
    regime_actuelle = models.CharField(("Régime actuel"), max_length=200, blank=True, null=True)
    note_alimentaion = models.TextField(("Note particulière concernant l'alimentation"), blank=True, null=True)
    conclusion = models.CharField(("Conclusion"), max_length=100, choices=constants.ALIMENTATION_CONCLUSION, default="normocalorique")
    raison_modification = models.TextField(("Raison de la modification"), blank=True, null=True)
    
    def __str__(self):
        return f"Historique de l'alimentation de {self.alimentation.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"   
    class Meta:
        verbose_name = "Historique de l'alimentation"
        verbose_name_plural = "Historiques de l'alimentation"
        models.indexes = [
            models.Index(fields=['alimentation', 'created_at']),
        ]