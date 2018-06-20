from django.db import models

__all__ = (
    'BlogUser',
    'UserInfo',
)

class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        blank=True,
        null=True,
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    @property
    def comments(self):
        result = f'{self.name}이 남긴 댓글 :\n'
        for comment in self.comment_set.all():
            result += f'- {comment}\n'
        return print(result)

    @property
    def posts(self):
        result = f'{self.name}이 작성한 글 :\n'
        for post in self.post_set.all():
            result += f'- {post}\n'
        return print(result)


class UserInfo(models.Model):
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user}님의 정보'

