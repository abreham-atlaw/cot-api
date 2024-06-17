from utils.web3.repositories.web3_repository import Web3Repository


class Web3ModelRepository(Web3Repository):
    def __init__(self, abi, address, serializer):
        super().__init__(abi, address)
        self.serializer = serializer
        self.attach_mode = True

    def get_by_id(self, id):
        contract = self.get_read_contract()
        response = contract.functions.getById(id).call()
        instance = self.serializer.deserialize(response)
        self.prepare_instance(instance)
        return instance

    def get_all(self):
        contract = self.get_read_contract()
        response = contract.functions.getAll().call()
        instances = self.serializer.deserialize_many(response)
        filtered = []
        for instance in instances:
            self.prepare_instance(instance)
            if self.filter_all(instance):
                filtered.append(instance)
        return filtered

    def prepare_instance(self, instance):
        if self.attach_mode:
            self.attach_foreign_keys(instance)

    def attach_foreign_keys(self, instance):
        pass

    def filter_all(self, instance):
        return True

