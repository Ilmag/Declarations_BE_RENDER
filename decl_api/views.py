from rest_framework import generics
from .models import Declaration
from .serializers import DeclarationSerializer
from .paginators import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend

class DeclarationList(generics.ListCreateAPIView):
    queryset = Declaration.objects.all().order_by('last_name', 'first_name', 'birth_date', 'birth_place',
                                                  'organization_txt', 'submited_at')
    serializer_class = DeclarationSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name']
