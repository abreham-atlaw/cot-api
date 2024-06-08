import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Summary
from apps.core.serializers import SummarySerializer
from di.utils_provider import UtilsProvider
from utils.pdfgen import ReportPDFGenerator


class GenerateReportView(APIView):

	__generator = ReportPDFGenerator()
	__file_storge = UtilsProvider.provide_file_storage()

	def post(self, request, *args, **kwargs):

		serializer = SummarySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		file_path = self.__generator.generate_bmc(serializer.validated_data)

		self.__file_storge.upload_file(file_path)
		url = self.__file_storge.get_url(os.path.basename(file_path))

		return Response(
			data={
				"link": url
			},
			status=status.HTTP_201_CREATED
		)
