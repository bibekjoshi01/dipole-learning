from django.contrib import admin
from core_app.models import (
    Category,
    Subject,
    Unit,
    Chapter,
    Heading,
    Sub_Heading,

)

class UnitInline(admin.TabularInline):  
    model = Unit

class CategoryModelAdmin(admin.ModelAdmin):
    ordering = ['id']

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    inlines = [UnitInline]
    ordering = ['id']

class UnitModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject']
    ordering = ['id']

class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit']
    ordering = ['id']

class HeadingModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'chapter']
    ordering = ['id']

class Sub_HeadingModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'heading']
    ordering = ['id']


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Unit, UnitModelAdmin)
admin.site.register(Chapter, ChapterModelAdmin)
admin.site.register(Heading, HeadingModelAdmin)
admin.site.register(Sub_Heading, Sub_HeadingModelAdmin)
