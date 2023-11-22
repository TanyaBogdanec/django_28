from django.urls import path
from .views import view_task

urlpatterns = [
    path('view_task/', view_task)
]