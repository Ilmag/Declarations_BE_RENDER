from django.urls import path
from decl_api import views

urlpatterns = [
    path('api/all', views.DeclarationList.as_view(), name='all'),
    path('api/gifts', views.GiftList.as_view(), name='gifts'),
    path('api/decl_gifts', views.DeclarationWithGifts.as_view(), name='decl_gifts'),
    path('api/declarants', views.DeclarantList.as_view(), name='declarants'),
    path('api/organizations', views.OrganizationList.as_view(), name='organizations'),
    path('api/sum_declarant_gifts', views.DeclarantSumGifts.as_view(), name='declarant_gifts_sum')
]