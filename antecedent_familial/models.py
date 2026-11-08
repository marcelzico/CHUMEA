from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants
# Create your models here.
class PersonneContacter(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    nom_prenom = models.CharField(("Nom et prénom(s)"), max_length=200)
    lien = models.CharField(("Lien avec l'enfant"), max_length=50, choices=constants.CONTACT_CHOIX, default="parents")
    tel1 = models.CharField(("Numéro téléphone opérationnel"), max_length=10)
    tel2 = models.CharField(("Numéro téléphone opérationnel"), max_length=10, blank=True, null=True)
    tel3 = models.CharField(("Numéro téléphone opérationnel"), max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    
class PersonneContacterHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass
    

class Social (UUIDPrimaryKeyModel, TimeStampedModel):
    nom_mere = models.CharField(_("Nom et prénom(s) de la mère"), max_length=200)
    age_mere = models.IntegerField()
    profession_mere = models.CharField(("Profession de la mère"))
    education_mere = models.CharField(("Niveau d'éducation"), max_length=50, choices=constants.EDUCATION_CHOIX)
    mere_vivant = models.BooleanField(("Vivant"), default=True)
    
    nom_pere = models.CharField(_("Nom et prénom(s) de la mère"), max_length=200)
    age_pere = models.IntegerField()
    profession_pere = models.CharField(("Profession de la mère"))
    education_pere = models.CharField(("Niveau d'éducation"), max_length=50, choices=constants.EDUCATION_CHOIX)
    pere_vivant = models.BooleanField(("Vivant"), default=True)
    
    statut_marital = models.CharField(("Statut marital"), max_length=50, choices=constants.STATUT_MARITAL_CHOIX)
    
    maison = models.CharField(("Type de maison"), max_length=50, choices=constants.TYPE_MAISON_CHOIX)
    nombre_chambre = models.IntegerField(("Nombre de chambre"))
    nombre_personne = models.IntegerField(("Nombre de personne"))    
    
    eau = models.CharField(("Eau"), max_length=50, choices=constants.EAU_CHOIX)
    eau_personnalise = models.BooleanField(("Eau personnalisée"), default=False)
    utilise_eau_javel = models.BooleanField(("Utilise l'eau de javel"), default=False)
    eau_boulli = models.BooleanField(("Faire boullir l'eau avant consommation"), default=True)
    note_eau = models.TextField(("Note particulière sur l'eau"), blank=True, null=True)
    
    toilette = models.CharField(("Toilette"), max_length=50, choices=constants.TYPE_TOILETTE_CHOIX)
    toilette_commun = models.BooleanField(("Toilette commun"), default=False)
    note_toilette = models.TextField(("Note particulière sur la toilette"), blank=True, null=True)
    
    eclairage = models.CharField(("Eclairage"), max_length=50, choices=constants.ECLAIRAGE_CHOIX)
    combustible = models.CharField(("Combustible"), max_length=50, choices=constants.COMBUSTIBLE_CHOIX)
    cuisine_separe = models.BooleanField(("Cuisine séparée"), default=True)
    note_combustible = models.TextField(("Note particulière sur les combustible et cuisine"), blank=True, null=True)
    
    niveau_social = models.CharField(("Combustible"), max_length=50, choices=constants.NIVEAU_SOCIAL_CHOIX)
    
    
class SocialHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class AntecedentFamilial(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    rang = models.CharField(("Rang dans la fratérie"), max_length=10)
    sante_ascendant = models.TextField(("Etat de la santé de son ascendance vis à vis de la pathologie actuelle"), blank=True, null=True)
    sante_collateral = models.TextField(("Etat de la santé de son collatéral vis à vis de la pathologe actuelle"), blank=True, null=True)
    
    diabete = models.BooleanField(("Diabète"), null=True, blank=True)
    diabete_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de la dibète"), blank=True, null=True)
    
    hta = models.BooleanField(("Hypertension artérielle"), null=True, blank=True)
    hta_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de l'hypertention artérielle"), blank=True, null=True)
    
    cardiopathie = models.BooleanField(("Cardiopathie"), null=True, blank=True)
    cardiopathie_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de la cardiopathie"), blank=True, null=True)
    
    epilepsie = models.BooleanField(("Epilepsie"), null=True, blank=True)
    epilepsie_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de l'épilepsie"), blank=True, null=True)
    
    nephropathie = models.BooleanField(("Néphropathie"), null=True, blank=True)
    nephropathie_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de la néphropathie"), blank=True, null=True)
    
    drepanocytose = models.BooleanField(("Drépanocytose"), null=True, blank=True)
    drepanocytose_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de la drépanocytose"), blank=True, null=True)
    
    hémophilie = models.BooleanField(("Hémophilie"), null=True, blank=True)
    hemophilie_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte de l'hémophilie"), blank=True, null=True)
    
    autre_pathologie = models.TextField(("Autre pathologie"), blank=True, null=True)
    autre_lien = models.CharField(("Lien parenté ou fraternel avec l'enfant et la personne atteinte"), blank=True, null=True)
    
    
class AntecedentFamilialHistoire(UUIDPrimaryKeyModel, TimeStampedModel):
    pass 
