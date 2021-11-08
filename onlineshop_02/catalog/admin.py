from django.contrib import admin
from .models import Category, Product

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug')
    list_filter = ('nama',)
    search_fields = ('nama',)
    prepopulated_fields={'slug': ('nama',)}
    ordering = ('nama',)

@admin.register(Product)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug', 'harga', 'available', 'created', 'update')
    list_filter = ('available', 'created', 'update')
    search_fields = ('body', 'nama')
    raw_id_fields = ('category',)
    prepopulated_fields= {'slug': ('nama',)}
    ordering = ('-created',)

