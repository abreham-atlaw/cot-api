from rest_framework import serializers

from apps.authentication.models import CoTUser
from apps.authentication.serializers import SymmetricKeySerializer


class KeyPairSerializer(serializers.Serializer):

	def __init__(self, password: str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__password = password

	def to_representation(self, instance: CoTUser):
		key_pair = CoTUser.objects.get_key_pair(instance, self.__password)
		return {
			"public": key_pair[0],
			"private": key_pair[1]
		}

