from django.urls import path
from .views import view_task


urlpatterns = [
    path('view_task/', view_task),
    path('view_create_task/', name='view_create_task'),
    path('create_task/', name='create_task'),
    path('task_detail/', name='task_detail'),
    path('update_task_status/', name='update_task_status'),
    path('add_comment_to_task/', name='add_comment_to_task'),

]

