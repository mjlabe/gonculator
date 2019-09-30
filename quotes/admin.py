from django import forms
from django.contrib import admin
import nested_admin

from quotes.models import *

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    search_fields = ['name']


@admin.register(POC)
class POCAdmin(admin.ModelAdmin):
    model = POC
    search_fields = ['name']


@admin.register(NWA)
class NWAAdmin(admin.ModelAdmin):
    model = NWA
    search_fields = ['nwa']


@admin.register(SerialNumber)
class SerialNumberAdmin(admin.ModelAdmin):
    model = SerialNumber


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    model = Component
    search_fields = ['name']


@admin.register(ArmoryComponent)
class ArmoryComponentAdmin(admin.ModelAdmin):
    model = ArmoryComponent


class ArmoryComponentsInline(nested_admin.NestedStackedInline):
    model = ArmoryComponent
    extra = 1


class ArmoryInline(nested_admin.NestedStackedInline):
    model = Armory
    extra = 1
    inlines = [ArmoryComponentsInline]
    readonly_fields = ['price']


@admin.register(Armory)
class ArmoryAdmin(admin.ModelAdmin):
    model = Armory
    inlines = [ArmoryComponentsInline, ]
    readonly_fields = ['price', ]


@admin.register(Quote)
class QuoteAdmin(nested_admin.NestedModelAdmin):
    model = Quote
    readonly_fields = ['quote_number', 'start', 'modified', 'complete', ]
    autocomplete_fields = ['project', 'nwa', 'user', 'poc', ]
    list_display = ['quote_number', 'project', 'modified', ]
    ordering = ['modified', ]
    inlines = [ArmoryInline]
