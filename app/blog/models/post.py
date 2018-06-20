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

class PostLike(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'포스트 {self.post}의 좋아요 수 : {len(self.objects.all())}'

