from django.urls import path
from decl_api import views

urlpatterns = [
    path('api/all', views.DeclarationList.as_view(),name='all'),
]