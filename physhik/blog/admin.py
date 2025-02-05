from django.contrib import admin

from .models import Category
from .models import Contact
from .models import Post
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "image",
        "live_site",
        "github_link",
        "description",
    )
    search_fields = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "overview",
        "body",
        "image",
        "created_on",
        "updated_on",
        "status",
    )
    list_filter = ("created_on", "updated_on")
    search_fields = ("slug",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "message")
    search_fields = ("name",)
