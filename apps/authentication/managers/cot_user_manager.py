import typing

from django.contrib.auth.models import BaseUserManager

from apps.authentication.models.organization_keys import SymmetricKey, PERMISSION_MAP
from utils.security import Encryptor
from utils.web3.repositories import ProfileRepository


class CoTUserManager(BaseUserManager):

	__profile_repository = ProfileRepository()

	def create_user(self, email, public_key: str, private_key: str, password: str=None, ):
		if not email:
			raise ValueError('Users must have a email')

		encryptor = Encryptor(password)

		user = self.model(
			email=email,
			public_key=encryptor.encrypt(public_key),
			private_key=encryptor.encrypt(private_key)
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def get_key_pair(self, user, password) -> typing.Tuple[str, str]:
		encryptor = Encryptor(password)
		return encryptor.decrypt(user.public_key), encryptor.decrypt(user.private_key)
	
	def set_password(self, user, old_password: str, new_password: str):
		old_encryptor = Encryptor(old_password)
		new_encryptor = Encryptor(new_password)
		
		user.public_key, user.private_key = [
			new_encryptor.encrypt(old_encryptor.decrypt(key))
			for key in [user.public_key, user.private_key]
		]

		user.set_password(new_password)
		user.save()

	def get_contract_keys(self, user, password) -> typing.List[SymmetricKey]:
		public_key, _ = self.get_key_pair(user, password)
		profile = self.__profile_repository.get_by_user_key(public_key)
		allowed_contracts = PERMISSION_MAP[profile.role]
		return SymmetricKey.objects.filter(contract__in=allowed_contracts, organization_key__organization_id=profile.organization_id)
