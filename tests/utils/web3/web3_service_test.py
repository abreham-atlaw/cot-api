import typing
import unittest

from di.utils_provider import UtilsProvider


class Web3ServiceTest(unittest.TestCase):
	
	__PUBLIC_KEY_LENGTH = 42
	__PRIVATE_KEY_LENGTH = 66
	
	def test_functionality(self):
		
		service = UtilsProvider.provide_web3_service()
		response = service.create_account()
		self.assertIsInstance(response, typing.Tuple)
		public_key, private_key = response
		self.assertIsInstance(public_key, str)
		self.assertIsInstance(private_key, str)
		self.assertEqual(len(public_key), self.__PUBLIC_KEY_LENGTH)
		self.assertEqual(len(private_key), self.__PRIVATE_KEY_LENGTH)
