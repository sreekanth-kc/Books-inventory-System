from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('book_management/', include('book_management.urls')),
    path('admin/', admin.site.urls),
]