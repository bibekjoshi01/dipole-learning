from django.contrib import admin
from django import forms
from . models import (
    Post,
    Comment,
    Category, 
    Tag,

)

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'slug': forms.TextInput(attrs={'readonly':'readonly'}),
        }

class PostModelAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at', 'is_publised')



admin.site.register(Post, PostModelAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

