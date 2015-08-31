from django.contrib import admin

from sorl.thumbnail.shortcuts import get_thumbnail

from blog.post.models import (
    Category, Post,
    PostReference, PostVideo, PostFile
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    search_fields = ('name', 'is_active', )


class PostReferenceInline(admin.StackedInline):
    model = PostReference
    extra = 0


class PostVideoInline(admin.StackedInline):
    model = PostVideo
    extra = 0


class PostFileInline(admin.StackedInline):
    model = PostFile
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'img_post',
        'title', 'start_date', 'end_date',
        'category', 'author', 'is_active',
    )
    search_fields = ('title', 'category', 'author', 'is_active')
    list_filter = ('category', 'author')
    inlines = (PostReferenceInline, PostVideoInline, PostFileInline)

    def img_post(self, obj):
        if obj.image:
            return "<img src='%s' />" % (
                get_thumbnail(
                    obj.image,
                    '100x66',
                    crop='center'
                ).url,

            )

    img_post.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
