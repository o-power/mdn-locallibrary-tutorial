"""locallibrary URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Add URL maps to redirect the base URL to our application
from django.views.generic.base import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

from django.conf import settings
from django.conf.urls.static import static

# If django.contrib.staticfiles is included in INSTALLED_APPS, Django will serve static files in DEBUG mode
# If django.contrib.staticfiles is not included in INSTALLED_APPS, uncomment the below to serve static files in DEBUG mode
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)

# Django does not serve media files in DEBUG mode unless the code below is uncommented
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
