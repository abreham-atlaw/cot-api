from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import CoTUser
from apps.authentication.serializers import ChangePasswordSerializer


class ChangePasswordView(APIView):

	def post(self, request, *args, **kwargs):

		serializer = ChangePasswordSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user = CoTUser.objects.get(email=serializer.validated_data.pop("email"))

		CoTUser.objects.set_password(
			user,
			**serializer.validated_data
		)

		return Response(
			data="Password Reset successfull",
			status=status.HTTP_200_OK
		)

