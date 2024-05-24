from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import ResetToken


class ResetPasswordSerializer(serializers.Serializer):

	token = serializers.CharField()
	password = serializers.CharField(min_length=8)

	def validate_token(self, value):
		token = ResetToken.objects.filter(token=value, used=False)
		if not token.exists():
			raise ValidationError("Invalid Token")
		token: ResetToken = token[0]
		if token.has_expired:
			raise ValidationError("Invalid Token")
		return token
