from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import CoTUser


class RequestPasswordResetSerializer(serializers.Serializer):

	email = serializers.EmailField()

	def validate_email(self, value):
		if not CoTUser.objects.filter(email=value).exists():
			raise ValidationError("User with this email doesn't exist")
		return value
