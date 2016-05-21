from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^groupname/(?P<groupname>[a-zA-Z0-9_]+)', views.groupname,
                                                    name='groupname'),
    url(r'^restore_password/', views.restore_password, name='restore_password'),
    url(r'^$', views.main, name='main'),
    url(r'^(?P<path>.+)', views.main_with_path, name='main_with_path'),
]
