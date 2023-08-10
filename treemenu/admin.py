from django.contrib import admin
from .models import Scheme
from mptt.admin import MPTTModelAdmin


class SchemeAdmin(MPTTModelAdmin):
    list_display = ('name', 'number', 'parent')
    search_fields = ['name']


admin.site.register(Scheme, SchemeAdmin)