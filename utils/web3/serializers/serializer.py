


from typing import List, Union, Optional
from datetime import datetime

from utils.web3.models import Profile


class Serializer:
    def __init__(self):
        pass

    def serialize(self, instance):
        raise NotImplementedError("Subclasses must implement this method")

    def deserialize(self, data):
        raise NotImplementedError("Subclasses must implement this method")

    def serialize_many(self, instances):
        return [self.serialize(instance) for instance in instances]

    def deserialize_many(self, data):
        return [self.deserialize(data) for data in data]


class NullableSerializer:

    def serialize(self, value):
        return value if value is not None else ""

    def deserialize(self, value):
        return value if value else None