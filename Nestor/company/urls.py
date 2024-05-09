
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='company_index'),
    path('<int:id>', views.get_company_by_id, name="company_page"),
    path('create_company', views.create_company, name="create_company")
]