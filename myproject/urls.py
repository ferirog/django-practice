"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from boardsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='board_topics'),
    path('about/', views.about, name = 'about'),
    path('about/company/', views.about_company, name = 'about_company'),
    # path('about/author/', views.about_author, name = 'about_author'),
    # path('about/author/ferirog/', views.about_ferirog, name = 'about_ferirog'),
    # path('about/author/ihwanes', views.about_ihwanes, name = 'about_ihwanes'),
    # path('privacy/', views.privacy, name = 'privacy'),
    # path('(?P<username>[\w.@+-]+)/', views.user_profile, name='user_profile'),

    # path('^boards/(?P<pk>\d+)/$', views.board_topics, name= 'board_topics'),
]
