from django.contrib import admin
from apps.galeria.models import Fotografia

# superuser: gustavo
# password: 123456

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario',)
    list_editable = ('publicada',)
    list_per_page = 20


admin.site.register(Fotografia, ListandoFotografias)
