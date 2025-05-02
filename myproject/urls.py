from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),  # for debug toolbar
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
