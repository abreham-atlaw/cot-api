import json

from utils.localization.llm import LLM
from utils.localization.translator import Translator


class LLMTranslator(Translator):

	def __init__(self, llm: LLM):
		self.__llm = llm
		self.__cache = {}

	def __from_cache(self, message: str, source_lang: str, target_lang: str) -> str:
		return self.__cache.get((message, source_lang, target_lang))

	def __store_cache(self, message: str, source_lang: str, target_lang: str, translation: str):
		self.__cache[(message, source_lang, target_lang)] = translation

	def __prepare_prompt(self, message: str, source_lang: str, target_lang: str) -> str:
		return f"""
Translate from {source_lang} to {target_lang}: {message}.
Format your answer in the following JSON format:

{{
	"source": "{source_lang}",
	"target": "{target_lang}",
	"text": "<TRANSLATED TEXT>"
}}
"""

	def __extract_response(self, response: str) -> str:
		return json.loads(response)["text"]

	def translate(self, text: str, source_lang: str, target_lang: str) -> str:
		cached = self.__from_cache(text, source_lang, target_lang)
		if cached is not None:
			return cached

		prompt = self.__prepare_prompt(text, source_lang, target_lang)
		response = self.__llm.chat(
			message=prompt
		)
		self.__store_cache(text, source_lang, target_lang, response)
		output = self.__extract_response(response)
		return output
