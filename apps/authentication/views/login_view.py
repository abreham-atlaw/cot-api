from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import KeyPairSerializer


class LoginView(APIView):

	def __send_invitation(self, email, link):
		send_mail(
			subject="Invitation",
			message=f"{link}",
			from_email="grandbwk@grandbluenet.com",
			recipient_list=[email],
			fail_silently=False
		)

	def post(self, request, *args, **kwargs):
		username = request.data.get('email')
		password = request.data.get('password')

		user = authenticate(request, username=username, password=password)

		if user is None:
			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

		serializer = KeyPairSerializer(instance=user, password=password)

		return Response(
			data=serializer.data,
			status=status.HTTP_200_OK
		)
