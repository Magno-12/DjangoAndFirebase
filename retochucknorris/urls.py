"""retochucknorris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from os import stat
import django
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path(r'admin/', admin.site.urls),
	path(r'', views.signIn),
    path(r'postsignIn/', views.postsignIn),
    path(r'button/', views.button, name="joke"),
    path(r'buttonFav/', views.buttonFav),
    path(r'list_Of_Jokes/', views.list_Of_Jokes),
    path(r'ButtonDelete/<str:id>', views.ButtonDelete),
    path('logout/', views.logout, name="log"),
]

