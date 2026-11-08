from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from patient.models import IdentifiantUniquePatient
from utilisateur.models import Doctor
import constants

# Create your models here.
class Prescription(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    date_prescription = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    import constants 

    def __str__(self):
        return f"Prescription {self.id} for {self.patient}"
    
class PrescriptionItem(UUIDPrimaryKeyModel, TimeStampedModel):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    forme_galenique = models.CharField(max_length=100, choices=constants.FORME_GALENIQUE_CHOICES)
    frequency = models.CharField(max_length=100)
    administration_route = models.CharField(max_length=100, choices=constants.ADMINISTRATION_ROUTE_CHOICES)
    duration = models.CharField(max_length=100)
    raison = models.TextField(blank=True, null=True)
    dispense = models.BooleanField(default=True)
    repetition_dispense = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    administre = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.medication_name} for Prescription {self.prescription.id}"
    

class PrescriptionHistory(UUIDPrimaryKeyModel, TimeStampedModel):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Prescription {self.prescription.id} - Action: {self.action}"
    
class PrescriptionItemHistory(UUIDPrimaryKeyModel, TimeStampedModel):
    prescription_item = models.ForeignKey(PrescriptionItem, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Prescription Item {self.prescription_item.id} - Action: {self.action}"
    

class AutreTraitement(UUIDPrimaryKeyModel, TimeStampedModel):
    patient = models.ForeignKey(IdentifiantUniquePatient, on_delete=models.CASCADE, related_name='autres_traitements')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='autres_traitements')
    date_traitement = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Autre Traitement {self.id} for {self.patient}"


class AutreTraitementHistory(UUIDPrimaryKeyModel, TimeStampedModel):
    autre_traitement = models.ForeignKey(AutreTraitement, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Autre Traitement {self.autre_traitement.id} - Action: {self.action}"
    
class Administration(UUIDPrimaryKeyModel, TimeStampedModel):
    prescription_item = models.ForeignKey(PrescriptionItem, on_delete=models.CASCADE, related_name='administrations')
    date_administration = models.DateTimeField(auto_now_add=True)
    administered_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Administration for Prescription Item {self.prescription_item.id} on {self.date_administration}"



