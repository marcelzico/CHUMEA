from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
import constants

# Create your models here.
class Langage(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    # 0 - 3 mois
    
    # 4 - 6 mois
    
    # 7 - 9 mois
    
    # 10 - 12 mois
    
    # 13 - 15 mois
    
    # 17 - 18 mois
    
    # 19 - 24 mois 
    
    

class LangageHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class Motricite (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    # 0 - 3 mois
    
    # 4 - 6 mois
    
    # 7 - 9 mois
    
    # 10 - 12 mois
    
    # 13 - 15 mois
    
    # 17 - 18 mois
    
    # 19 - 24 mois 



class MotriciteHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class Prehension (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    # 0 - 3 mois
    
    # 4 - 6 mois
    
    # 7 - 9 mois
    
    # 10 - 12 mois
    
    # 13 - 15 mois
    
    # 17 - 18 mois
    
    # 19 - 24 mois 
        


class PrehensionHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class Relationnelle (UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.ForeignKey.PROTECT)
    # 0 - 3 mois
    
    # 4 - 6 mois
    
    # 7 - 9 mois
    
    # 10 - 12 mois
    
    # 13 - 15 mois
    
    # 17 - 18 mois
    
    # 19 - 24 mois 
        

class RelationnelleHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass


class TannerGarcon (UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Pour les garçons pubère
    """ 
    pass

class TannerGarconHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass 


class TannerFille (UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Pour les filles pubère
    """ 
    pass


class TannerFilleHistoire (UUIDPrimaryKeyModel, TimeStampedModel):
    pass

