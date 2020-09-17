"""ensemble_monday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", include("daemun.urls")),
    #path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    #path("polls/", include("polls.urls")),
    path("faq/", include("faq.urls")),
    path("team/", include("team.urls")),
    path("gadmin/", include("gsheets.urls")),
    path("updates/", include("updates.urls")),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
