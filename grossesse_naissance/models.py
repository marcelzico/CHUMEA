from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants

# Create your models here.
class Grossesse (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    gravida = models.IntegerField(("Nombre de gossesse"))
    parite = models.IntegerField(("Nombre de parité"))
    avortement = models.IntegerField(("Nombre d'avortement"))
    nombre_enfant = models.IntegerField(("Nombre d'enfant vivant"))
    
    cpn_debut = models.CharField(("Date ou moins de début de CPN"), max_length=100, null=True, blank=True)
    cpn_nombre = models.IntegerField(("Nombre de CPN"), null=True, blank=True)
    cpn_rythme = models.CharField(("Rythme de CPN"), max_length=100, null=True, blank=True)
    cpn_lieu = models.CharField(("Lieu de CPN"), max_length=100, null=True, blank=True)
    
    vat_nombre = models.IntegerField(("Nombre de VAT"), null=True, blank=True)
    
    serologie_faite = models.TextField(("Serologie faite"), null=True, blank=True)
    serologie_resultat = models.TextField(("Résultat de serologie"), null=True, blank=True)
    
    echographie_nombre = models.IntegerField(("Nombre d'échographie"), null=True, blank=True)
    echographie_resultat = models.CharField(("Résultat d'échographie"), max_length=200, null=True, blank=True)

    pathologie_grossesse = models.TextField(("Pathologie de grossesse"), null=True, blank=True)
    
    leucorrhee_couleur = models.CharField(("Couleur de leucorrhée"), max_length=100, null=True, blank=True)
    leucorrhee_odeur = models.CharField(("Odeur de leucorrhée"), max_length=100, null=True, blank=True)
    leucorrhee_quantite = models.CharField(("Quantité de leucorrhée"), max_length=100, null=True, blank=True)
    leucorrhee_traitee = models.BooleanField(("Traitement de leucorrhée"), default=False, null=True, blank=True)
    
    prise_medicament = models.TextField(("Prise de médicament"), null=True, blank=True)
    prise_toxique = models.TextField(("Prise de toxique"), null=True, blank=True)
    
    note_grossesse = models.TextField(("Note particulière pour la grossesse"), blank=True, null=True)
    conclusion = models.CharField(("Conclusion"), max_length=200, choices=constants.CONCLUSION_GROSSESSE, null=True, blank=True)
    


class GrossesseHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class Accouchement(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    lieu = models.CharField(("Lieu d'accouchement"), max_length=100, null=True, blank=True)
    travail_dure = models.CharField(("La durée du travail"), max_length=100, blank=True, null=True)
    poussee_duree = models.CharField(("La durée des poussées"), max_length=100, blank=True, null=True)
    
    la_aspect = models.CharField(("Aspect de liquide amniotique"), max_length=100, choices=constants.LIQUIDE_AMNIOTIQUE_ASPECT, default="clair")
    la_odeur = models.CharField(("Odeur de liquide amniotique"), max_length=100, choices=constants.LIQUIDE_AMNIOTIQUE_COULEUR, default="inodore")
    la_quantite = models.CharField(("Quantité de liquide amniotique"), max_length=100, choices=constants.LIQUIDE_AMNIOTIQUE_QUANTITE, default="normale")
    
    voie = models.CharField(("Voie de l'accouchement"), max_length=10, choices=constants.VOIE_ACCOUCHEMENT, default="basse")
    
    cri = models.BooleanField(("Cri immédiat"), null=True, blank=True, default=True)
    asphyxie =  models.BooleanField(("Asphyxie néonatale"), null=True, blank=True, default=True)
    reanimation = models.BooleanField(("Notion de réanimation néonatale"), null=True, blank=True, default=True)
    reanimation_duree = models.IntegerField(("Durée de réanimation en minute"), null=True, blank=True)
    mode_accouchement = models.CharField(("Mode d'accouchement (eutocique/dystocique)"), max_length=20, choices=constants.MODE_ACCOUCHEMENT, default="eutocique")
    
    apgar_indice = models.IntegerField(("Score d'APGAR"), null=True, blank=True)
    
    terme = models.CharField(("Terme de l'accouchement"), default="terme", choices=constants.TERME_ACCOUCHEMENT)
    poids_naissance = models.IntegerField(("Poids à la naissance en gramme (g)"))
    trophie = models.CharField(("Trophie de l'enfant"), max_length=30, choices=constants.TROPHIE, default="normotophie")
    
    
class AccouchementHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass 
    