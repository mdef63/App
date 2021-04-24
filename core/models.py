from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.CharField(
        max_length=2000,
        help_text='Комментарий к пользователю'
    )