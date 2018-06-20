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

    def __str__(self):
        return f'{self.user}님의 댓글'

    @property
    def like_users(self):
        result = '이 댓글에 좋아요를 누른 사람:\n'
        for post_like in CommentLike.objects.filter(comment_id=self.id):
            result += f'- {post_like.user}\n'
        return print(result)

class CommentLike(Base):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}님이 님의 댓글을 좋아합니다.'
