from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser, UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Model representing a user in the system.
    Inherits from AbstractUser for built-in user functionality,
    UUIDPrimaryKeyModel for UUID primary key, and TimeStampedModel for created/updated timestamps.
    """
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_practitioner = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    """
    Model representing additional profile information for a user.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
    
class Doctor(models.Model):
    """
    Model representing a doctor in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialty}"
    
class Nurse(models.Model):
    """
    Model representing a nurse in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='nurse_profile')
    department = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Nurse {self.user.username} - {self.department}"
    
class Patient(models.Model):
    """
    Model representing a patient in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='patient_profile')
    medical_record_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Patient {self.user.username} - MRN: {self.medical_record_number}"
    
class Administrator(models.Model):
    
    """
    Model representing an administrator in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='admin_profile')
    role_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Administrator {self.user.username}"
    
class Intern(models.Model):
    """
    Model representing an intern in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='intern_profile')
    internship_start_date = models.DateField(null=True, blank=True)
    internship_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Intern {self.user.username} - Internship: {self.internship_start_date} to {self.internship_end_date}"

class Student(models.Model):
    
    """
    Model representing a student in the system.
    Linked to the Utilisateur model via a one-to-one relationship.
    """
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_number = models.CharField(max_length=50, unique=True)
    course_of_study = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Student {self.user.username} - Enrollment: {self.enrollment_number}"
    

