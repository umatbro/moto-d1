import io
import sys
import unittest
from bank.bank import Account
from datetime import date
from unittest import mock


class TestPrinter:
    def __init__(self):
        self.message = None

    def print(self, message):
        print(message)
        self.message = message


class BankTest(unittest.TestCase):
    def test_print_header(self):
        account = Account()
        self.assertEqual('DATE | AMOUNT | BALANCE', str(account))

    def test_deposit(self):
        account = Account()
        account.deposit(100)
        self.assertEqual(100, account.balance)
        account.deposit(200)
        self.assertEqual(300, account.balance)

    def test_print_transaction(self):
        account = Account()
        account.deposit(100, date(2017, 2, 1))
        account.deposit(200, date(2017, 3, 1))
        account.deposit(-100, date(2017, 4, 1))

        captured_output = io.StringIO()
        sys.stdout = captured_output
        account.print()
        # sys.stdout = sys.__stdout__
        captured_output.seek(0)
        val = captured_output.read()

        self.assertEqual(
            'DATE | AMOUNT | BALANCE\n'
            '01/02/2017 | 100 | 100\n'
            '01/03/2017 | 200 | 300\n'
            '01/04/2017 | -100 | 200\n', val
        )

    def test_print_transaction_with_mock(self):
        account = Account()
        account.deposit(100, date(2017, 2, 1))
        account.deposit(200, date(2017, 3, 1))
        account.deposit(-100, date(2017, 4, 1))

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            account.print()

        val = fake_stdout.getvalue()

        self.assertEqual(
            'DATE | AMOUNT | BALANCE\n'
            '01/02/2017 | 100 | 100\n'
            '01/03/2017 | 200 | 300\n'
            '01/04/2017 | -100 | 200\n', val
        )


if __name__ == '__main__':
    unittest.main()
