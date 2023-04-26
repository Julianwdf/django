from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    # open dictionary with key as slug and tuple category name, rmb the comma
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
