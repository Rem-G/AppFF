from django.urls import re_path

from . import views

app_name = 'dictionnaire_ta'

urlpatterns = [
    re_path(r'^$', views.accueil_doc, name='accueil_doc'),
    re_path(r'^table/(?P<table>[A-z0-9_]+)/(?P<variable_recherche>[A-z0-9_ ]{0,})$', views.doc_table, name='doc_table'),
    re_path(r'^recherche/$', views.recherche, name='recherche'),
]
