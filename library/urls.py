"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import settings
from books.views import books
from books import mylogin, easy_login

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'books/', include('books.urls')),
    
    # django contrib login - commented for now in favor of easy login.
    # path(r'accounts/', include("django.contrib.auth.urls")),  # new
    # path(r'register/', mylogin.register_request),

    # easy login implementation
    path(r'elogin/', easy_login.elogin, name='elogin'),
    path(r'eregister/', easy_login.eregister, name='eregister'),
    path(r'logout/', easy_login.mylogout, name='logout'),
    path(r'api/', include('api.urls')),

    path(r'', login_required(books, login_url='elogin')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
