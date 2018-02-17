from datetime import date, datetime

HEADER = 'DATE | AMOUNT | BALANCE\n'


class Account:
    def __init__(self, init_amount=0):
        self.init_amount = init_amount
        self.transactions = []

    @property
    def balance(self):
        balance = self.init_amount
        for transaction in self.transactions:
            balance += transaction[1]

        return balance

    def deposit(self, value, transaction_date=datetime.now().date()):
        if not isinstance(value, int) or not isinstance(transaction_date, date):
            raise ValueError('Incorrect inputs: {}, {}'.format(value, transaction_date))
        self.transactions.append((transaction_date, value))

    def withdraw(self, value, transaction_date=datetime.now().date()):
        self.deposit(-value, transaction_date)

    def __str__(self):
        result = HEADER
        balance = self.init_amount

        for transaction in self.transactions:
            tdate, amount = transaction
            balance += amount
            result += '{date} | {amount} | {balance}\n'.format(
                date=tdate.strftime('%d/%m/%Y'),
                amount=amount,
                balance=balance
            )

        return result.strip()

    def print(self):
        print(self)
