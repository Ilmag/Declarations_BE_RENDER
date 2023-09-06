from django.urls import path
from decl_api import views

urlpatterns = [
    path('api/', views.DeclarationList.as_view(),name='all'),
]