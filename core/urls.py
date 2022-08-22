"""core URL Configuration

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
from turtle import home
from django.contrib import admin
from django.urls import path
from core.views import ProteinAbbsorbanceTimePointThresholdFilter, UploadFileView, ProteinInfo, ProteinTimePointAbsorbance, ProteinAbbsorbanceTimePointFilter, ProteinWithSpecificProcessFunciton
from core.models import Protein

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home),
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('list/', ProteinAbbsorbanceTimePointThresholdFilter.as_view(), name='list'),
    path('info/', ProteinInfo.as_view(), name='info'),
    path('time-point/', ProteinTimePointAbsorbance.as_view(), name='time-point'),
    path('single-field-time-point/', ProteinAbbsorbanceTimePointFilter.as_view(), name='single-field-time-point'),
    path('process/', ProteinWithSpecificProcessFunciton.as_view(), name='process')
]
