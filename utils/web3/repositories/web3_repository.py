from web3 import Web3
from web3.middleware import geth_poa_middleware
import uuid

from di.utils_provider import UtilsProvider


class Web3Repository:
    def __init__(self, abi, address):
        self.provider = UtilsProvider.provider_ether_provider()
        self.address = address
        self.abi = abi
        self._provider_contract = None

    def get_read_contract(self):
        if self._provider_contract is None:
            self._provider_contract = self.provider.eth.contract(address=self.address, abi=self.abi)
        return self._provider_contract

