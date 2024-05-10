from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applicant_index'),
    path('applicant', views.applicant, name='applicant')
]
