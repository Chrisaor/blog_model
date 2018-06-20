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
    def number_like(self):
        return f'{len(PostLike.objects.filter(post_id=self.id))}'

    @property
    def like_users(self):
        result = '이 포스트에 좋아요를 누른 사람:\n'
        for post_like in PostLike.objects.filter(post_id=self.id):
            result += f'- {post_like.user}\n'
        return print(result)

class PostLike(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'좋아요!'

