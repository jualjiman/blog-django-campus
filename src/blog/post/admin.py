from django.contrib import admin
from blog.post.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    search_fields = ('name', 'is_active', )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'start_date', 'end_date',
        'category', 'author', 'is_active'
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
