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
    path('application/<int:id>', views.apply_init, name='apply/init'),
    path('application/experience_add/<int:id>', views.application_experience_add, name='application/experience_add'),
    path('application/education_add/<int:id>', views.application_education_add, name='application/education_add'),
    path('application/reference_add/<int:id>', views.application_reference_add, name='application/reference_add'),
    path('application/experience_edit/<int:id>', views.application_experience_edit, name='application/experience_edit'),
    path('application/education_edit/<int:id>', views.application_education_edit, name='application/education_edit'),
    path('application/reference_edit/<int:id>', views.application_reference_edit, name='application/reference_edit'),
    path('application/add_skill/<int:id>', views.add_skill, name='application/add_skill')
]
