import typing

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from apps.authentication.managers.cot_user_manager import CoTUserManager


class CoTUser(AbstractBaseUser):
	USERNAME_FIELD = 'email'

	full_name = models.CharField(max_length=64)
	email = models.EmailField(unique=True)

	public_key = models.BinaryField()
	private_key = models.BinaryField()

	is_admin = models.BooleanField(default=False)

	objects = CoTUserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
