from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import CoTUser


class ChangePasswordSerializer(serializers.Serializer):

	email = serializers.EmailField()
	old_password = serializers.CharField()
	new_password = serializers.CharField(min_length=8)

	def validate(self, attrs):
		if authenticate(username=attrs.get("email"), password=attrs.get("old_password")) is None:
			raise ValidationError("Incorrect Old Password")
		if attrs.get("old_password") == attrs.get("new_password"):
			raise ValidationError("New password can't be the same as old password.")
		return attrs

	def validate_email(self, value):
		if not CoTUser.objects.filter(email=value).exists():
			raise ValidationError("A user with this email doesn't exist.")
		return value
