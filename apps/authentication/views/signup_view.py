from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import CoTUser
from apps.authentication.serializers import SignupSerializer, KeyPairSerializer
from di.utils_provider import UtilsProvider


class SignupView(APIView):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__w3_service = UtilsProvider.provide_web3_service()

	def post(self, request, *args, **kwargs):

		serializer = SignupSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		email = serializer.validated_data.get("email")
		if serializer.validated_data.get("invitation"):
			email = serializer.validated_data.get("invitation").email

		public_key, private_key = self.__w3_service.create_account()

		user = CoTUser.objects.create_user(
			public_key=public_key,
			private_key=private_key,
			email=email,
			password=serializer.validated_data["password"]
		)

		serializer = KeyPairSerializer(instance=user, password=serializer.validated_data["password"])

		return Response(
			data=serializer.data,
			status=status.HTTP_201_CREATED
		)
