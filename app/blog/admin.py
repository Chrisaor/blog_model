from django.contrib import admin

from blog.models import Post, PostLike, BlogUser, UserInfo, Comment, CommentLike, Base

admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(BlogUser)
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(CommentLike)