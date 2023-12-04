from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_task/', include("view_task.urls"),
    path('app/', include('user.urls')))
]
