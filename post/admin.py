from django.contrib import admin
from .models import Post, PostLike, PostComment, CommentLike

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "caption", "created_at")
    search_fields = ("author", "caption", "author__username")

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "created_at")
    search_fields = ("id", "author__username")

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "created_at")
    search_fields = ("id", "author__username", "comment")

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'created_at')
    search_fields = ('id', 'author__username')

admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)