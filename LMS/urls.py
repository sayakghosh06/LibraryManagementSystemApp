"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.library_management, name='library_management')
Class-based views
    1. Add an import:  from other_app.views import library_management
    2. Add a URL to urlpatterns:  path('', library_management.as_view(), name='library_management')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Library Management System Admin"
admin.site.site_title = "Library Management System Admin Portal"
admin.site.index_title = "Welcome to Library Management System Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library_management.urls"))  

]
