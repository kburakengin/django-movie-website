from django.contrib import admin
from .models import Movies


#
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','is_published')
    list_display_links = ('id','name')  # link olusturma
    list_filter = ('created_date',) # filtreleme islemi
    list_editable = ('is_published',)  # editable alan , tick ekle kaldir
    search_fields = ('name', 'description')
    list_per_page = 20

# Register your models here.

admin.site.register(Movies, MovieAdmin)
