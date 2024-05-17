from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13)
    date_of_birth = models.DateField(null=True)
    photo = models.ImageField(upload_to='user_photos', default='default-pics/img.png', blank=True, null=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ConfirmationCodeModel(models.Model):
    code = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.email}"

    def __repr__(self):
        return f"{self.code} - {self.email}"

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'
