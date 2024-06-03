import typing

from django.contrib.auth.models import BaseUserManager

from utils.security import Encryptor


class CoTUserManager(BaseUserManager):

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
