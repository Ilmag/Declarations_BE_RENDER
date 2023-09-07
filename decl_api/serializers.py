from rest_framework import serializers
from .models import Declaration

class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = ['id', 'decl_id', 'first_name', 'last_name','organization_txt',
                  'position', 'birth_place', 'birth_date', 'submited_at']