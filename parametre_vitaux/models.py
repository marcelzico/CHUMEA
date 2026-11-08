from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient

# Create your models here.
class ParametreVitaux(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.PROTECT, related_name='parametre_vitaux')
    probleme = models.ForeignKey('probleme.Problem', on_delete=models.PROTECT, related_name='parametre_vitaux', null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    tension_arterielle_systolique = models.CharField(max_length=20, null=True, blank=True)
    tension_arterielle_diastolique = models.CharField(max_length=20, null=True, blank=True)
    frequence_cardiaque = models.IntegerField(null=True, blank=True)
    frequence_respiratoire = models.IntegerField(null=True, blank=True)
    saturation_oxygene = models.FloatField(null=True, blank=True)
    glycemie = models.FloatField(null=True, blank=True)
    date_mesure = models.DateField(null=True, blank=True)
    temps_de_mesure = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Paramètre Vital"
        verbose_name_plural = "Paramètres Vitaux"

    def __str__(self):
        return f"Paramètres vitaux de {self.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class ParametreVitauxHistorique(UUIDPrimaryKeyModel, TimeStampedModel):
    parametre_vitaux = models.ForeignKey(ParametreVitaux, on_delete=models.CASCADE, related_name='historique')
    temperature = models.FloatField(null=True, blank=True)
    tension_arterielle_systolique = models.CharField(max_length=20, null=True, blank=True)
    tension_arterielle_diastolique = models.CharField(max_length=20, null=True, blank=True)
    frequence_cardiaque = models.IntegerField(null=True, blank=True)
    frequence_respiratoire = models.IntegerField(null=True, blank=True)
    saturation_oxygene = models.FloatField(null=True, blank=True)
    glycemie = models.FloatField(null=True, blank=True)
    date_mesure = models.DateField(null=True, blank=True)
    temps_de_mesure = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Historique des Paramètres Vitaux"
        verbose_name_plural = "Historiques des Paramètres Vitaux"

    def __str__(self):
        return f"Historique des paramètres vitaux de {self.parametre_vitaux.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    

class Anthropometrie(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.PROTECT, related_name='anthropometrie')
    poids = models.FloatField(null=True, blank=True)
    taille = models.FloatField(null=True, blank=True)
    perimetre_cranien = models.FloatField(null=True, blank=True)
    perimetre_abdominal = models.FloatField(null=True, blank=True)
    perimetre_brachial = models.FloatField(null=True, blank=True)
    poids_sur_taille = models.FloatField(null=True, blank=True)
    taille_sur_age = models.FloatField(null=True, blank=True)
    imc = models.FloatField(null=True, blank=True)
    date_mesure = models.DateField(null=True, blank=True)
    temps_de_mesure = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Anthropométrie"
        verbose_name_plural = "Anthropométries"

    def __str__(self):
        return f"Anthropométrie de {self.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class AnthropometrieHistorique(UUIDPrimaryKeyModel, TimeStampedModel):
    anthropometrie = models.ForeignKey(Anthropometrie, on_delete=models.CASCADE, related_name='historique')
    poids = models.FloatField(null=True, blank=True)
    taille = models.FloatField(null=True, blank=True)
    perimetre_cranien = models.FloatField(null=True, blank=True)
    perimetre_abdominal = models.FloatField(null=True, blank=True)
    perimetre_brachial = models.FloatField(null=True, blank=True)
    poids_sur_taille = models.FloatField(null=True, blank=True)
    taille_sur_age = models.FloatField(null=True, blank=True)
    imc = models.FloatField(null=True, blank=True)
    date_mesure = models.DateField(null=True, blank=True)
    temps_de_mesure = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Historique de l'Anthropométrie"
        verbose_name_plural = "Historiques de l'Anthropométrie"

    def __str__(self):
        return f"Historique de l'anthropométrie de {self.anthropometrie.patient} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

