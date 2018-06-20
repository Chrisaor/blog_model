from django.db import models

from blog.models import BlogUser, Base

__all__ = (
    'Post',
    'PostLike',
)

class Post(Base):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'

    @property
    def post_like(self):
        return f'이 포스트의 좋아요 수 : {len(PostLike.objects.filter(post_id=self.id))}'

class PostLike(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'좋아요!'

