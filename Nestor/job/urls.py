from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job_index'),
    path('<int:id>', views.get_job_by_id, name="job_page"),
    path('create_job', views.create_job, name="create_job"),
    path('favorite_jobs', views.favorite_jobs, name="favorite_jobs"),
    path('applied_jobs', views.applied_jobs, name="applied_jobs"),
    path('favorite_job', views.favorite_job, name="favorite_job"),
    path('your_job_offers', views.your_job_offers, name="your_job_offers"),
    path('your_job_offers/<int:id>', views.get_applications_by_job_id, name="applications_page"),
    path('your_job_offers/<int:jid>/application/<int:aid>', views.review_application, name="review_application"),
]
