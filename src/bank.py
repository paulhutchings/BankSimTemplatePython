"""
 @author Cay Horstmann
 @author Modified by Paul Wolfgang
 @author Modified by Charles Wang
 @author Modified by Alexa Delacenserie
 @author Modified by Tarek Elseify
 @author Modified by Paul Hutchings
"""
from account import Account

class Bank:
    N_TEST = 10
    def __init__(self, num_accounts, initial_balance):
        """
        Creates and returns a new Bank object
        """
        self._num_transactions = 0
        self._initial_balance = initial_balance
        self._num_accounts = num_accounts
        self._accounts = [Account(i, initial_balance) for i in range(num_accounts)]

    def get_num_accounts(self):
        """
        Returns the number of accounts in the bank
        """
        return len(self._accounts)

    def transfer(self, from_acc, to_acc, amount):
        """
        Transfers money from one account to another
        """
        if self._accounts[from_acc].withdrawal(amount):
            self._accounts[to_acc].deposit(amount)

        # Uncomment below when ready to start Task 3
        # if self.should_test():
        #     self.test()
        
    def should_test(self):
        """
        Returns True if the bank needs to be tested, otherwise False
        """
        self._num_transactions += 1
        return self._num_transactions % N_TEST == 0
    
    def test(self):
        """
        Sums the balances of all the accounts and prints whether
        or not the total amount has changed.
        """
        [print(account.to_string()) for account in self._accounts]
        balances = [account.get_balance() for account in self._accounts]
        total_balance = sum(balances)
        print(f'Total balance: {total_balance}')
        if total_balance == self._num_accounts * self._initial_balance:
            print('Total balance unchanged')
        else:
            print('Total balance changed!')