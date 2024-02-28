from django.contrib import admin
from tekken.models import Tekken

# Register your models here.

class TekkenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nacionalidade', 'estilo_de_luta')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('nacionalidade',)
    list_editable = ('nacionalidade',)
    list_per_page = 10
    ordering = ('nome', )


admin.site.register(Tekken, TekkenAdmin)