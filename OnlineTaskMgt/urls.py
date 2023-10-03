"""
URL configuration for OnlineTaskMgt project.

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
from django.urls import path
from TaskApp import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add_project/', views.add_project, name='add_project'),
    path('remove_project/<int:project_id>/', views.remove_project, name='remove_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
]



