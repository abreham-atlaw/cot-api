from utils.web3.models import Profile
from utils.web3.serializers.serializer import NullableSerializer, Serializer


class ProfileSerializer(Serializer):
    def __init__(self):
        super().__init__()
        self.nullable_string_serializer = NullableSerializer()

    def serialize(self, instance):
        return [
            instance.role,
            instance.id,
            instance.name,
            instance.user_key,
            instance.email,
            self.nullable_string_serializer.serialize(instance.organization_id) if instance.organization_id else None,
            self.nullable_string_serializer.serialize(instance.department_id) if instance.department_id else None
        ]

    def deserialize(self, data):
        return Profile(
            name=data[2],
            role=data[0],
            user_key=data[3],
            email=data[4],
            organization_id=self.nullable_string_serializer.deserialize(data[5]) if data[5] else None,
        )
