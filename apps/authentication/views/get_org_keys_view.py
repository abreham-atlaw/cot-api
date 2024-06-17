from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models.organization_keys import PERMISSION_MAP, OrganizationKeys
from apps.authentication.serializers import SymmetricKeySerializer


class GetOrgKeysView(APIView):

    def get(self, request, *args, **kwargs):

        organization_id = request.query_params.get("organization_id")
        organization_keys = OrganizationKeys.objects.get(organization_id=organization_id).keys.filter(
            contract="profile"
        )
        serializer = SymmetricKeySerializer(instance=organization_keys, many=True)

        return Response(
            data=serializer.data
        )
