"""pratice_1 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
#from pra_app_1 import views
# from pra_app_2 import views as p_2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^morning/', views.display),
    # url(r'^evening/', p_1.dis),
    # url(r'^even/', p_2.greeting),
    url(r'^pra_app_1/', include('pra_app_1.url')),
    url(r'^pra_app_2/', include('pra_app_2.url1')),
    # url(r'^pra_app_1/', include('pra_app_1.urls')),
]
