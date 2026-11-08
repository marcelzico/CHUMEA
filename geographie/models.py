from django.db import models
from modele_partager.models import UUIDPrimaryKeyModel, TimeStampedModel

class Province(UUIDPrimaryKeyModel, TimeStampedModel):
    nom = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=32, blank=True)  # official code if any
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "geo_province"
        ordering = ["nom"]


class Region(UUIDPrimaryKeyModel, TimeStampedModel):
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name="regions"
    )
    nom = models.CharField(max_length=128)
    code = models.CharField(max_length=32, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "geo_region"
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
                fields=["province", "nom"],
                nom="unique_region_per_province"
            )
        ]


class District(UUIDPrimaryKeyModel, TimeStampedModel):
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, related_name="districts"
    )
    nom = models.CharField(max_length=128)
    code = models.CharField(max_length=32, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "geo_district"
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
                fields=["region", "nom"],
                nom="unique_district_per_region"
            )
        ]


class Commune(UUIDPrimaryKeyModel, TimeStampedModel):
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name="communes"
    )
    nom = models.CharField(max_length=128)
    code = models.CharField(max_length=32, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "geo_commune"
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
                fields=["district", "nom"],
                nom="unique_commune_per_district"
            )
        ]


class Fokontany(UUIDPrimaryKeyModel, TimeStampedModel):
    """
    Lowest level. Not always known (there are > 10 000 in the country).
    Stored when available.
    """
    commune = models.ForeignKey(
        Commune, on_delete=models.PROTECT, related_name="fokontany_list"
    )
    nom = models.CharField(max_length=128)
    code = models.CharField(max_length=32, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "geo_fokontany"
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
                fields=["commune", "nom"],
                nom="unique_fokontany_per_commune"
            )
        ]
        
    