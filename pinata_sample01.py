import unittest
import os

from pinatapy import PinataPy


class TestPinataPy(unittest.TestCase):
    def setUp(self) -> None:
        api_key = os.environ.get("PINATA_API_KEY")
        secret_key = os.environ.get("PINATA_SECRET_API_KEY")
        api_key = "a109870f8c80ed4af901"
        secret_key = "3ac524fe52bf622a3b099b5807fc7d5d8b628f707720717e8b6b0e66248dcc89"
        if api_key and secret_key:
            self.pinata = PinataPy(api_key, secret_key)
        else:
            raise ValueError("No API keys in environment variables")

    def test_remove_pin_from_ipfs(self) -> None:
        pass

    def test_pin_list(self) -> None:
        options = {"status": "pinned"}
        res = self.pinata.pin_list(options)
        self.assertIn("rows", res)

    def test_user_pinned_data_total(self) -> None:
        res = self.pinata.user_pinned_data_total()
        self.assertIn("pin_count", res)


if __name__ == "__main__":
    unittest.main()
