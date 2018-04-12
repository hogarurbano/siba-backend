"""uh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import include, path
from django.contrib.auth import views
from datetime import datetime

import apps.appweb.views
import apps.appweb.forms

urlpatterns = [
    path('', apps.appweb.views.home, name='home'), # importing HomePage to AppWeb
    path('contact', apps.appweb.views.contact, name='contact' ),
     path('about', apps.appweb.views.about, name='about' ),

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),

    path('login/',
        views.login,
        {
            'template_name': 'appweb/login.html',
            'authentication_form': apps.appweb.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'year': datetime.now().year,
                'title': 'Log in',
            }
        },
        name='login'),

    path('logout',
        views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]

