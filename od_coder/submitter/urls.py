from django.urls import path

from . import views

app_name = 'submitter'
urlpatterns = [
        path('', views.index, name = 'index'),
        path('<int:task_id>/task/', views.task_detail, name='task'),
]
