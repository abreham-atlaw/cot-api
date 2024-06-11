from cot.settings import ETHER_NODE_URL, EMAIL_SOURCE, EMAIL_TEMPLATE_DIR, DRIVE_HOST, GEMINI_API_KEY, LLM_TEMPERATURE
from utils.file_storage import FileStorage
from utils.file_storage.file_storages import HostingStorage
from utils.localization.gemini import Gemini
from utils.localization.llm import LLM
from utils.localization.llm_translator import LLMTranslator
from utils.localization.translator import Translator
from utils.mail.mail_client import MailClient
from utils.web3.web3_service import Web3Service


class UtilsProvider:

	@staticmethod
	def provide_web3_service() -> Web3Service:
		return Web3Service(node=ETHER_NODE_URL)

	@staticmethod
	def provide_mail_client() -> MailClient:
		return MailClient(
			source=EMAIL_SOURCE,
			template_dir=EMAIL_TEMPLATE_DIR,
		)

	@staticmethod
	def provide_file_storage() -> FileStorage:
		return HostingStorage(DRIVE_HOST)

	@staticmethod
	def provide_llm() -> LLM:
		return Gemini(
			token=GEMINI_API_KEY,
			temperature=LLM_TEMPERATURE
		)

	@staticmethod
	def provide_translator() -> Translator:
		return LLMTranslator(UtilsProvider.provide_llm())
