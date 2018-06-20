from django.db import models

__all__ = (
    'BlogUser',
    'UserInfo',
)

class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user}님의 정보'

class Relation(models.Model):
    CHOICE_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='relation_by_from_user',
    )

    to_user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='relation_by_to_user',
    )

    relation_type = models.CharField(
        max_length=1,
        choices=CHOICE_RELATION_TYPE,
    )

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )
