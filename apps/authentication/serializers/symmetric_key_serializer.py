from rest_framework import serializers

from apps.authentication.models.organization_keys import SymmetricKey


class SymmetricKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = SymmetricKey
        fields = ["key", "contract"]
