from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password,  **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address.')
        email=self.normalize_email(email)
        user = self.model(
            email=email,
            last_login=now,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email,password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

        
class User(AbstractBaseUser,PermissionsMixin):
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    EMAIL_FIELD='email'

    class Meta:
        verbose_name = 'account'  
        verbose_name_plural = 'accounts'
 