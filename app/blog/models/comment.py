from django.db import models

from blog.models import Base, BlogUser
from blog.models.post import Post

__all__ = (
    'Comment',
    'CommentLike',
)

class Comment(Base):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class CommentLike(Base):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

