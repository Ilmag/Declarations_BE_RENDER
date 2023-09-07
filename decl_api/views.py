from rest_framework import generics
from .models import Declaration, Gift, Declarant, Organization
from .serializers import DeclarationSerializer, GiftSerializer, DeclaratnSerializer, OrganizationSerializer, DeclGiftSerializer,GiftSerializer,DeclaratnSerializer, DeclGiftSerializer, DeclarantGiftSerializer
from .paginators import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum

class DeclarationList(generics.ListCreateAPIView):
    queryset = Declaration.objects.all().order_by('last_name', 'first_name', 'birth_date', 'birth_place',
                                                  'organization', 'submited_at')
    serializer_class = DeclarationSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name']

class GiftList(generics.ListCreateAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer


class DeclarationWithGifts(generics.ListCreateAPIView):
    queryset = Declaration.objects.filter(gifts__isnull = False).order_by('declarant')
    serializer_class = DeclGiftSerializer


class DeclarantList(generics.ListCreateAPIView):
    queryset = Declarant.objects.all().order_by('last_name', 'first_name', 'birth_date')
    serializer_class = DeclaratnSerializer


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer


class DeclarantSumGifts(generics.ListCreateAPIView):
    queryset = Gift.objects.values('declarant_id').order_by('declarant_id').annotate(sum_lari = Sum('lari'))
    serializer_class = DeclarantGiftSerializer