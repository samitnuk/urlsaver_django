from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_view, name='main'),
    url(r'^(?P<path>.+)', views.main_view_with_path, name='main_with_path'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]
