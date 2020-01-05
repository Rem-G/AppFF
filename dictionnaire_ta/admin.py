#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Variable, OrdreTables
from django.forms import TextInput, Textarea
from django.db import models

# action d'administration pour copier des enregistrements existants
def copier_enregistrement(modeladmin, request, queryset):
    for objet in queryset:
        objet.id = None
        objet.save()
copier_enregistrement.short_description = 'Copier les enregistrements sélectionnées'

class VariableAdmin(admin.ModelAdmin):
    """
    Administration de la class Variable, permet la visualisation des variables existantes, l'édition et la création de nouvelles variables
    """
    list_display = ('id', 'numero', 'nom', 'description', 'observation', 'formule_ini', 'origine', 'nature', 'lgr', 'table_associee')
    list_display_links = ('nom',)
    ordering = (('table_associee', ))
    search_fields = ('nom', 'table_associee',)
    
    fieldsets = (
       ('Général', {
            'classes': ['wide', 'extrapretty',],
            'fields': ('numero', 'nom', 'description', 'observation', 'formule_ini', 'origine', 'nature', 'lgr', 'table_associee')
        }),
    )
    
class OrdreTablesAdmin(admin.ModelAdmin):
    list_display = ('table', 'liste')
    
    list_display_links = ('table',)
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'200'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    
    fieldsets = (
       ('Général', {
            'classes': ['wide', 'extrapretty',],
            'fields': ('table', 'liste')
        }),
    )
    
actions = [copier_enregistrement]
    
admin.site.register(OrdreTables, OrdreTablesAdmin)
admin.site.register(Variable, VariableAdmin)
