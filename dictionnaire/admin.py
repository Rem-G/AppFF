from django.contrib import admin

# Register your models here.
from .models import Variable, DescVariable, OrdreTables
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
    list_display = ('id','nom', 'description', 'observation', 'origine', 'type', 'millesime',
                     'fiabilite', 'doc', 'table_associee')
    list_display_links = ('nom',)
    ordering = ('numero', 'table_associee')
    search_fields = ('nom', 'table_associee',)
    
    fieldsets = (
       ('Général', {
            'classes': ['wide', 'extrapretty',],
            'fields': ('nom', 'description','observation', 'origine',  'type', 
                       'millesime', 'fiabilite', 'doc', 'table_associee', 'modalites')
        }),
    )
    filter_horizontal = ('modalites',)
    
class DescVariableAdmin(admin.ModelAdmin):
    list_display = ('code', 'var_associee', 'valeur', 'description','observation', 'millesime', 'table_var_associee')
    list_display_links = ('table_var_associee', 'var_associee')
    ordering = ('code', 'table_var_associee', 'var_associee')
    search_fields = ('var_associee', 'table_var_associee', 'code')
    
    fieldsets = (
       ('Général', {
            'classes': ['wide', 'extrapretty',],
            'fields': ('code', 'valeur', 'description','observation', 'millesime', 'var_associee', 'table_var_associee')
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

admin.site.register(Variable, VariableAdmin)
admin.site.register(DescVariable, DescVariableAdmin)
admin.site.register(OrdreTables, OrdreTablesAdmin)