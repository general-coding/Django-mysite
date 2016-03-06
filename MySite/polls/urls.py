'''
Created on Mar 6, 2016

@author: Puneeth U Bharadwaj
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]