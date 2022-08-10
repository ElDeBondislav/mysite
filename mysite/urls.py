from django.contrib import admin
from django.urls import path
from blog.views import home
from blog.views import ajax
from blog.views import mobile_login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', mobile_login),
    path('login/ajax', ajax),
]
