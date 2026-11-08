from django.db import models
import constants
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from geographie.models import Province, Region, District, Commune, Fokontany

# Create your models here.
class IdentifiantUniquePatient(UUIDPrimaryKeyModel, TimeStampedModel):
    "Les code d'identification à figurer (selon la date, ou donner une code pour chaque hopital ou utiliser code postal ou code CIN ou méthode combinée)"
    
    pass



class EtatCivil(UUIDPrimaryKeyModel, TimeStampedModel):
    identifiant = models.OneToOneField(IdentifiantUniquePatient)
    nom = models.CharField(_("Nom"), max_length=1001)
    prénom = models.CharField(("Prénom(s)"), max_length=100)
    genre = models.CharField(("Genre"), max_length=10, choices=constants.GENRE_CHOIX)
    ddn = models.DateField(_("Date de naissance"), auto_now=False, auto_now_add=False)
    ldn = models.CharField(_("Lieu de naissance"), max_length=50)
    age = models.CharField(_("Age"), max_length=10) # sera calculer automatique à partir de la date naissance
    adresse_commune = models.CharField(("Adresse (Commune)"), max_length=50)
    adresse_exacte = models.CharField(("Adresse complet"), max_length=100)



class EtatCivilHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class AdressePatient(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.PROTECT)
    """
    Province, région, disctrict seront apparu ici pour dans la formulaire pour facilité la sélection de commune car on a 6 provinces, 24 régions, 120 districts et 1695 communes, et defiler une liste de 1695 élements n'est pas pratique à chaque fois
    """
    commune = models.ForeignKey(Commune, verbose_name=_(""), on_delete=models.CASCADE)
    fokontany = models.CharField(("Fokontany"), max_length=100)
    lot_maison = models.CharField(("Adresse exact avec lot et nom de la ville ou village ou quartier"))
    


class AdressePatientHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass



