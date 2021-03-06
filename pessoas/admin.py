from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_links = ('nome','email')
    search_fields = ('nome',)

# Register your models here.
admin.site.register(Pessoa, ListandoPessoas)