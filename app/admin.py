# from django.contrib import admin
#
# from app.models import Blog
#
# # Register your models here.
#
# admin.site.register(Blog)


from django.contrib import admin

from app.models import News, Category,ContactData

# Register your models here.

# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

from django.contrib import admin
from .models import Video

admin.site.register(Video)

admin.site.register(ContactData)


