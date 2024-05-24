from django.db import models

import secrets

from django.utils import timezone

from cot.settings import RESET_TOKEN_LIFETIME
from .cot_user import CoTUser


def generate_token(length=32) -> str:
	token = secrets.token_hex(length)
	return token


class ResetToken(models.Model):

	token: str = models.CharField(max_length=255, default=generate_token)
	user: CoTUser = models.ForeignKey(CoTUser, on_delete=models.CASCADE)
	create_datetime = models.DateTimeField(auto_now_add=True)
	used = models.BooleanField(default=False)

	@property
	def has_expired(self) -> bool:
		return (timezone.now() - self.create_datetime).total_seconds() > RESET_TOKEN_LIFETIME
