"""
URL configuration for converter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home),
    path("pdf_to_jpg/", views.PDFJPG),
    path("jpg-to_png/", views.JPGPNG),
    path("youtube_downloader/", views.YOUTUBE),
    path("404_page/", views.NotFound),
]
