# _*_ encoding:utf-8 _*
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    user
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="user's real name")
    birthday = models.DateField(null=True, blank=True, verbose_name="user's birthday")
    mobile = models.CharField(max_length=11, verbose_name="user's tel number")
    gender = models.CharField(max_length=6, choices=(("male", "MAN"), ("female", "WOMAN")), default="WOMAN")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="user's email address")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"verify code")
    mobile = models.CharField(max_length=11, verbose_name="user's tel number")
    add_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = "verify code"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.mobile)
