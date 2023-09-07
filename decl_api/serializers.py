from rest_framework import serializers
from .models import Declaration, Gift, Declarant, Organization

class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = ['id', 'decl_id', 'first_name', 'last_name','organization_txt',
                  'position', 'birth_place', 'birth_date', 'submited_at']
        

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'


class DeclaratnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declarant
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class DeclGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = ['id', 'decl_id', 'declarant', 'first_name', 'last_name', 'organization',
                  'organization_txt', 'position', 'birth_date', 'submited_at', 'gifts']
        

class DeclarantGiftSerializer(serializers.ModelSerializer):
    sum_lari = serializers.IntegerField()
    class Meta:
        model = Gift
        fields = ['declarant_id','sum_lari']