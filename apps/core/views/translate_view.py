from rest_framework.response import Response
from rest_framework.views import APIView

from di.utils_provider import UtilsProvider


class TranslateView(APIView):

	__translator = UtilsProvider.provide_translator()

	def post(self, request, *args, **kwargs):
		text = request.data.get('text')
		source_lang = request.data.get('source_lang')
		target_lang = request.data.get('target_lang')

		translated_text = self.__translator.translate(text, source_lang, target_lang)

		return Response({'text': translated_text})
