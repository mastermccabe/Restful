"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^new$', views.new, name = 'new_user'),
    url(r'^create$', views.create, name = 'adduser'),
    url(r'^(?P<user_id>\d+)$', views.show),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    # url(r'^activity', views.activity, name = 'activity'),   extra , name='my_edit'
    url(r'^(?P<user_id>\d+)/delete$', views.delete),

]
