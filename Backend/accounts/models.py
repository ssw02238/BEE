from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, nickname, password=None):

        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):

        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']


# ESG 성향 테스트 추가
class MBTI(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # mbti 점수
    e_score = models.FloatField(default=0)
    s_score = models.FloatField(default=0)
    g_score = models.FloatField(default=0)

    # mbti 기반 추천 기업
    first = models.IntegerField(blank=True, null=True)
    second = models.IntegerField(blank=True, null=True)
    third = models.IntegerField(blank=True, null=True)