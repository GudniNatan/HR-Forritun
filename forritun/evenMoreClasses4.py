class Account(object):
    INTEREST_PAID = 1.0
    BONUS_RATE = 1.0

    def __init__(self, balance):
        self.balance = balance

    def update_balance(self):
        bonus = (self.balance * self.BONUS_RATE) - self.balance
        self.balance = (self.balance * self.INTEREST_PAID) + bonus

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)


class SavingsAccount(Account):
    INTEREST_PAID = 1.05
    BONUS_RATE = 1.1


class DebitAccount(Account):
    INTEREST_PAID = 1.02


def print_accounts(account_list):
    for account in account_list:
        print(account)


def update_accounts(account_list):
    for account in account_list:
        account.update_balance()


def main():
    s1 = SavingsAccount(1000)
    d1 = DebitAccount(1000)
    s2 = SavingsAccount(2000)
    d2 = DebitAccount(4000)

    accounts = [s1, d1, s2, d2]

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

main()
