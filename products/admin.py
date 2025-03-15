from django.contrib import admin

from .models import Product, Comment


class CommentsInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ['author', 'text', 'stars', 'active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status']
    inlines = [CommentsInlineAdmin]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'text', 'stars', 'active']

    def get_queryset(self, request):
        return Comment.all_comments.all()
