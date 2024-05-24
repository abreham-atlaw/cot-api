import typing

from web3 import Web3


class Web3Service:

	def __init__(self, node: str):
		self.__client = Web3(Web3.HTTPProvider(node))

	def create_account(self) -> typing.Tuple[str, str]:
		account = self.__client.eth.account.create()
		return account.address, account.key.hex()
