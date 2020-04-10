from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('table/',include('table.urls')),
    path('item/',include('table.urls')),
]
