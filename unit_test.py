import unittest
from banking_system import BankSystem, BankAccount


class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        """Setup a fresh bank system before each test."""
        self.bank = BankSystem()

    def test_create_account_valid(self):
        account_id = self.bank.create_account("Alice", 1000)
        account = self.bank.get_account_by_id(account_id)
        self.assertEqual(account.name, "Alice")
        self.assertEqual(account.balance, 1000)

    def test_create_account_negative_balance(self):
        with self.assertRaises(ValueError):
            self.bank.create_account("Bob", -100)

    def test_deposit_valid(self):
        account_id = self.bank.create_account("Charlie", 1000)
        account = self.bank.get_account_by_id(account_id)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_deposit_invalid(self):
        account_id = self.bank.create_account("David", 1000)
        account = self.bank.get_account_by_id(account_id)
        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_withdraw_valid(self):
        account_id = self.bank.create_account("Eve", 1000)
        account = self.bank.get_account_by_id(account_id)
        account.withdraw(300)
        self.assertEqual(account.balance, 700)

    def test_withdraw_invalid(self):
        account_id = self.bank.create_account("Frank", 1000)
        account = self.bank.get_account_by_id(account_id)
        with self.assertRaises(ValueError):
            account.withdraw(-200)

    def test_transfer_valid(self):
        account_id_1 = self.bank.create_account("Grace", 1000)
        account_id_2 = self.bank.create_account("Hannah", 500)
        sender = self.bank.get_account_by_id(account_id_1)
        receiver = self.bank.get_account_by_id(account_id_2)
        sender.transfer(receiver, 200)
        self.assertEqual(sender.balance, 800)
        self.assertEqual(receiver.balance, 700)

    def test_transfer_invalid(self):
        account_id_1 = self.bank.create_account("Ivy", 1000)
        account_id_2 = self.bank.create_account("Jack", 500)
        sender = self.bank.get_account_by_id(account_id_1)
        receiver = self.bank.get_account_by_id(account_id_2)
        with self.assertRaises(ValueError):
            sender.transfer(receiver, 2000)

    def test_invalid_name_input(self):
        # Test invalid names (containing numbers or emojis)
        with self.assertRaises(ValueError):
            self.bank.create_account("Alice123", 500)

        with self.assertRaises(ValueError):
            self.bank.create_account("đ°Bob", 500)

    def test_invalid_deposit_amount(self):
        # Test invalid deposit amounts (non-numeric or negative)
        account_id = self.bank.create_account("Mike", 1000)
        account = self.bank.get_account_by_id(account_id)
        with self.assertRaises(ValueError):
            account.deposit("non-numeric")

        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_invalid_withdraw_amount(self):
        # Test invalid withdrawal amounts (non-numeric or negative)
        account_id = self.bank.create_account("Lily", 1000)
        account = self.bank.get_account_by_id(account_id)
        with self.assertRaises(ValueError):
            account.withdraw("non-numeric")

        with self.assertRaises(ValueError):
            account.withdraw(-100)

    def test_invalid_transfer_amount(self):
        # Test invalid transfer amounts (non-numeric or negative)
        account_id_1 = self.bank.create_account("John", 1000)
        account_id_2 = self.bank.create_account("Paul", 500)
        sender = self.bank.get_account_by_id(account_id_1)
        receiver = self.bank.get_account_by_id(account_id_2)
        with self.assertRaises(ValueError):
            sender.transfer(receiver, "non-numeric")

        with self.assertRaises(ValueError):
            sender.transfer(receiver, -100)


if __name__ == "__main__":
    unittest.main()