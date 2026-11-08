from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient


# Create your models here.
class HistoireMaladie(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.PROTECT, related_name='histoire_maladie')
    probleme = models.ForeignKey('probleme.Problem', on_delete=models.PROTECT, related_name='histoire_maladie', null=True, blank=True)
    ordre = models.IntegerField(null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    signes_symptomes = models.TextField(null=True, blank=True)
    signes_associes = models.TextField(null=True, blank=True)
    traitement = models.TextField(null=True, blank=True)
    evolution = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Histoire de la maladie de {self.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
    class Meta:
        verbose_name = "Histoire de la maladie"
        verbose_name_plural = "Histoires de la maladie"
        