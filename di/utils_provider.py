from web3 import Web3
from web3.middleware import geth_poa_middleware

from cot.settings import ETHER_NODE_URL, EMAIL_SOURCE, EMAIL_TEMPLATE_DIR, DRIVE_HOST
from utils.file_storage import FileStorage
from utils.file_storage.file_storages import HostingStorage
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
	def provider_ether_provider():
		w3 = Web3(Web3.HTTPProvider(ETHER_NODE_URL))
		w3.middleware_onion.inject(geth_poa_middleware, layer=0)
		return w3
