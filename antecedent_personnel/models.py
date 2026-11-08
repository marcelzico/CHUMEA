from django.db import models
from patient.models import EtatCivil, IdentifiantUniquePatient
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
import constants

# Create your models here.
class AntecedentMedical(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    contexte = models.TextField()
    
class AntecedentMedicalHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class AntecedentChirurgical(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    contexte = models.TextField()
    

class AntecedentChirurgicalHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass 


class MaladieChronique(UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Une maladie chronique ou héréditaire à la fois
    """
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    pathologie = models.TextField(("Pathologie"), help_text="Ex : diabète type I, HTA, Ashtme, Drépanocytose, Hémophilie, ...")
    traitement = models.TextField(("Traitements"), help_text="Lister tous les médicaments pour traiter la pathologie reçu par le/la patient(e).")
    medecin_traitant = models.TextField(("Médecin traitant (généraliste ou spécialiste) qui traite le patient pour ce pathologie"), help_text="Ex : Dr X, service/hopital/clinique/CSB/libre Y, lieu Z, contact ...", blank=True, null=True)
    connu_depuis = models.DateField(auto_now_add=False, auto_now=False)
    


class MaladieChroniqueHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class Allergie(UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Une allergie à la fois
    """
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    allergene = models.TextField(("Allergène"))
    classification = models.CharField(("Classification"), max_length=50, choices=constants.ALLERGIE_CLASSIFICATION_CHOIX)
    reaction = models.TextField(("Manifestion de la réaction allergique"))
    severite = models.CharField(("Sévérité"), max_length=50, choices=constants.ALLERGIE_SEVERITE_CHOIX)
    connu_depuis = models.DateField(auto_now_add=False, auto_now=False)
    

class AllergieHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class ImportanteInformation(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    groupe_sanguin = models.CharField(("Groupe sanguin"), max_length=10, choices=constants.GROUPE_SANGUIN)
