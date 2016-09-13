from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^login$', views.login_view, name = 'login'),
                url(r'^dashboard$', views.dashboard, name = 'dashboard'),
                url(r'^logout$', views.logout, name = 'logout'),
]