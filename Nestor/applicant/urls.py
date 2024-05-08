
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applicant_index'),
    path('profile/edit', views.applicant, name='profile/edit')
]
