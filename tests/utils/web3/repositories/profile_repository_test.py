import unittest

from utils.web3.repositories import ProfileRepository


class ProfileRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repository = ProfileRepository()

    def test_get_all_profiles(self):
        profiles = self.repository.get_all()

        self.assertNotEqual(len(profiles), 0)
