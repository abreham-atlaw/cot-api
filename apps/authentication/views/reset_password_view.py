from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import ResetToken
from apps.authentication.serializers import ResetPasswordSerializer


class ResetPasswordView(APIView):

	def post(self, request, *args, **kwargs):

		serializer = ResetPasswordSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user = serializer.validated_data["token"].user
		user.set_password(serializer.validated_data["password"])
		user.save()

		return Response(
			data="Password reset successful",
			status=status.HTTP_200_OK
		)
