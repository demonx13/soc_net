from django.contrib import admin

from .models import Post, Comment
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts
    """
    list_display = ("id", "user", "published", "create_date", "moderation", "view_count")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Comments to Posts
    """
    list_display = ("id", "user", "post", "published", "created_date", "update_date")

    # actions = ['unpubish', 'publish']
    mptt_level_indent = 15
