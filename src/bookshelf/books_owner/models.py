from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BooksOwnerManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        if not email:
            raise ValueError('You must have email address!')
        if not username:
            raise ValueError('You must have username')
        if not first_name:
            raise ValueError('You must have first name!')
        if not last_name:
            raise ValueError('You must have last name!')
        if not password:
            raise ValueError('You must have password!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(self, email, username, first_name, last_name, password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class BooksOwner(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)
    username = models.CharField(verbose_name='Username', max_length=50, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=50, unique=False)
    last_name = models.CharField(verbose_name='Last name', max_length=50, unique=False)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Date joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self):
        return self.is_admin

    # def has_module_perms(self):
    #     return True
