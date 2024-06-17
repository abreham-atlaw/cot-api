import json

from cot.settings import CONTRACTS_PATH
from utils.web3.repositories.web3_model_repository import Web3ModelRepository
from utils.web3.serializers.profile_repository import ProfileSerializer


class ProfileRepository(Web3ModelRepository):
    def __init__(self):
        with open(CONTRACTS_PATH / "src_contracts_Profile_sol_Profile.json", 'r') as file:
            contract_data = json.load(file)
        abi = contract_data['abi']
        address = contract_data['address']
        super().__init__(abi, address, ProfileSerializer())

    def get_by_user_key(self, key):
        contract = self.get_read_contract()
        response = contract.functions.getByUserKey(key).call()
        instance = self.serializer.deserialize(response)
        self.attach_foreign_keys(instance)
        return instance
