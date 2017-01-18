from django.conf.urls import url
from . import views

# https://docs.djangoproject.com/en/1.10/intro/tutorial03/

app_name = 'table'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(\w+)/$', views.index, name='index')
]