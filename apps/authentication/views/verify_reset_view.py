from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import ResetToken


class VerifyResetView(APIView):

	def get(self, request, *args, **kwargs):

		token:ResetToken = get_object_or_404(ResetToken, token=request.query_params.get("token"))
		if token.has_expired:
			return Response(
				data="Token as expired",
				status=status.HTTP_401_UNAUTHORIZED
			)

		return Response(
			data="Valid token",
			status=status.HTTP_200_OK
		)