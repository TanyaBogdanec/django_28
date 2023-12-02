from django.urls import path
from .views import view_task
from . import views

urlpatterns = [
    path('view_task/', view_task),
    path('view_task/', view_task)
]



# Настройте маршрутизацию (URL routing) в Django,
# чтобы пользователи могли получать доступ к каждому представлению (view) по правильному URL.

# эту задачу я не до конца поняла как сделать