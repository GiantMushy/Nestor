
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job_index'),
    path('<int:id>', views.get_job_by_id, name="job_page"),
    path('create_job', views.create_job, name="create_job"),
    path('favorite_jobs', views.favorite_jobs, name="favorite_jobs"),
    path('applied_jobs', views.applied_jobs, name="applied_jobs")
]