from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse

class UserManager(BaseUserManager):
    def _create_user(self, username, password, name, surname,
                     obligation, assigned_function, location, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            name=name,
            surname=surname,
            obligation=obligation,
            assigned_function=assigned_function,
            location=location,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    surname = models.CharField(max_length=254, null=True, blank=True)
    obligation = models.CharField(max_length=50, null=True)
    assigned_function = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=256, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'login_user'

    def get_absolute_url(self):
        return reverse('form-list')
