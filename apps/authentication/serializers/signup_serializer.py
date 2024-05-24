from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import CoTUser, Invitation


class SignupSerializer(serializers.Serializer):

	invitation = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Invitation.objects.all())
	email = serializers.EmailField(allow_null=True)
	password = serializers.CharField(min_length=8)

	def validate_email(self, value: str):
		if CoTUser.objects.filter(email=value).exists():
			return ValidationError("User with this email already exits")
		return value
