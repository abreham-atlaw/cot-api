import os.path

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import CoTUser, ResetToken
from apps.authentication.serializers import RequestPasswordResetSerializer
from cot.settings import FRONTEND_URL
from di.utils_provider import UtilsProvider


class RequestPasswordResetView(APIView):

	__mail_client = UtilsProvider.provide_mail_client()

	def post(self, request, *args, **kwargs):

		serializer = RequestPasswordResetSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user: CoTUser = CoTUser.objects.get(email=serializer.validated_data["email"])

		token: ResetToken = ResetToken.objects.create(
			user=user
		)

		self.__mail_client.send_reset_password_mail(
			to=user.email,
			link=f"{FRONTEND_URL}/auth/reset-password?token={token.token}"
		)

		return Response(
			data="URL Sent to email"
		)
