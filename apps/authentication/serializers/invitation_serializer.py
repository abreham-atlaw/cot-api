from rest_framework import serializers


class InvitationSerializer(serializers.Serializer):

	id = serializers.CharField()
	email = serializers.EmailField()
	link = serializers.CharField()
	organization = serializers.CharField()
