from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #menampilkan kolom yang direquest ke dalam user interface
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    #memfilter data sesuai kolom yang diinginkan, biasa muncul pada sidebar
    list_filter = ('status', 'created', 'publish', 'author')

    #memberikan fitur tambahan search sesuai dengan data kolom
    search_fields = ('title', 'body')

    #membuat nilai slug otomatis seperti title
    prepopulated_fields = {'slug': ('title',)}

    #memberikan lookup widget lebih baik memberi experience user
    raw_id_fields = ('author',)

    #memberi navigasi sesuai waktu publish
    date_hierarchy = 'publish'

    #mengurutkan data sesuai status dan publish nya
    ordering = ('status', 'publish')

# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nama', 'body', 'created', 'active')
    list_filter = ('post', 'nama', 'created')
    search_fields = ('body', 'nama')
    raw_id_fields = ('post',)
    ordering = ('created',)