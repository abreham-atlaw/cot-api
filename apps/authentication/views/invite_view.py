from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import Invitation
from apps.authentication.serializers.invitation_serializer import InvitationSerializer
from di.utils_provider import UtilsProvider


class InviteView(APIView):

	__mail_client = UtilsProvider.provide_mail_client()

	def post(self, request, *args, **kwargs):

		serializer = InvitationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		Invitation.objects.create(
			id=serializer.validated_data["id"],
			email=serializer.validated_data["email"],
		)

		self.__mail_client.send_invitation_mail(
			to=serializer.validated_data["email"],
			link=serializer.validated_data["link"],
			organisation=serializer.validated_data["organization"],
		)

		return Response("Invitation Sent", status=status.HTTP_200_OK)
