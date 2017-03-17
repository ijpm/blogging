from django.contrib import admin

from blogs.models import Categoria, Blog, Post


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name','description')

    fieldsets = (
        (None, {
            "fields": ("name",)
        }),
        ("description", {
            "fields": ("description",),
            "description": "escribe algo anda",
            "classes": ("collapse",)
        })
    )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'tematica', 'owner', 'created_at')
    list_filter = ('owner', 'tematica')
    search_fields = ('name', 'tematica')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'owner', 'created_at')