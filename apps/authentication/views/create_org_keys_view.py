from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from cryptography.fernet import Fernet

from apps.authentication.models.organization_keys import Contracts, SymmetricKey, OrganizationKeys
from apps.authentication.serializers import SymmetricKeySerializer


class CreateOrganizationKeysView(APIView):

    def __generate_key(self) -> str:
        return Fernet.generate_key().decode()

    def post(self, request: Request, *args, **kwargs):
        organization_id = request.data.get("organization_id")
        organization_key: OrganizationKeys = OrganizationKeys.objects.create(
            organization_id=organization_id
        )
        for contract in Contracts.all:
            SymmetricKey.objects.create(
                organization_key=organization_key,
                contract=contract,
                key=self.__generate_key()
            )

        serializer = SymmetricKeySerializer(instance=organization_key.keys, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

