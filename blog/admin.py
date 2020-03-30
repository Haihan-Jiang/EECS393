from django.contrib import admin
from .models import Post, room


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')

    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(room)
class PostAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'status', 'slug', 'roomType', 'roomID',
                    'price', )
    list_filter = ('status', )
    search_fields = ('hotel', 'roomID', 'roomType')
    prepopulated_fields = {'slug': ('hotel', 'roomType', 'roomID')}
    ordering = ('status', 'price')
