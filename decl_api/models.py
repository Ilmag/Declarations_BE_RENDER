from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizations'


class Declarant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    birth_place = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField()

    class Meta:
        db_table = 'declarants'


class Gift(models.Model):
    decl_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    type_choices = models.CharField(max_length=2, choices=GIFT_TYPE_CHOICES, null=True, blank=True)
    declarant = models.BooleanField(default=False)
    declarant_id = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    relationship = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=3, null=True, blank=True)
    owner_first_name = models.CharField(max_length=20, blank=True, null=True)
    owner_last_name = models.CharField(max_length=40, blank=True, null=True)
    owner_id = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    relation_name = models.CharField(max_length=20, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    lari = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'gifts'
        

class Declaration(models.Model):
    declarant = models.ForeignKey(Declarant, on_delete=models.CASCADE)
    decl_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    organization_txt = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    birth_place = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField()
    updated_at = models.DateField(null=True, blank=True)
    submited_at = models.DateField()
    gifts = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        saxeli = f'{self.first_name} {self.last_name}'
        return saxeli
    
    class Meta:
        db_table = 'declarations'