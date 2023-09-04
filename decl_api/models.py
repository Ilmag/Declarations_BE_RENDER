from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Declaration(models.Model):
    decl_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
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