"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello word!')

def hello_python(request):
    return HttpResponse('Hello python!!')

def articles_str(request, data):
    return HttpResponse('Hello articles +++ ' + data)

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)

urlpatterns = [
    path('', hello, name='home'),
    path('python/', hello_python),
    re_path(r'^articles/(?P<data>\w+)/$', articles_str),
    re_path(r'^sum/(?P<a>\d+)/(?P<b>\d+)/$', sum_two),
    path('admin/', admin.site.urls),
]
