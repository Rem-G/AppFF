from django.urls import re_path

from . import views

app_name = 'dictionnaire'

urlpatterns = [
    re_path(r'^$', views.accueil_doc, name='accueil_doc'),
    re_path(r'^table/(?P<table>[A-z0-9_]+)/(?P<url_millesime>[A-z0-9_]{0,5})/(?P<variable_recherche>[A-z0-9_ ]{0,})$', views.doc_table, name='doc_table'),
    re_path(r'^variable/(?P<table>[0-9a-z_]+)/(?P<variable>[0-9a-z_]+)$', views.desc_var, name='desc_var'),
    re_path(r'^recherche/$', views.recherche, name='recherche'),
]
