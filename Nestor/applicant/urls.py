from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='applicant_index'),
    path('applicant', views.applicant, name='applicant'),
    path('applicant/contact-info', views.contact_info, name='applicant/contact-info'),
    path('applicant/experience_add', views.experience_add, name='applicant/experience_add'),
    path('applicant/education_add', views.education_add, name='applicant/education_add'),
    path('applicant/reference_add', views.reference_add, name='applicant/reference_add'),
    path('applicant/experience_edit', views.experience_edit, name='applicant/experience_edit'),
    path('applicant/education_edit', views.education_edit, name='applicant/education_edit'),
    path('applicant/reference_edit', views.reference_edit, name='applicant/reference_edit'),
    path('applicant/add_skill', views.add_skill, name='applicant/add_skill'),
    path('applicant/remove_skill', views.remove_skill, name='applicant/remove_skill'),
    path('application/<int:id>', views.apply_init, name='apply/init')
]
