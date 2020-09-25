 
"""
 @author Cay Horstmann
 @author Modified by Paul Wolfgang
 @author Modified by Charles Wang
 @author Modified by Alexa Delacenserie
 @author Modified by Tarek Elseify
 @author Modified by Paul Hutchings
"""
class Account:
    def __init__(self, id, initial_balance):
        """
        Creates and returns a new Account object
        """
        self._id = id
        self._balance = initial_balance

    def get_balance(self):
        """
        Returns the current balance in the account
        """
        return self._balance

    def withdrawal(self, amount):
        """
        Withdrawals money from the account
        """
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        """
        Deposits money into the account
        """
        self._balance += amount

    def to_string(self):
        """
        Returns the account information as a formatted string
        """
        return f'Account[{self._id}] balance: {self._balance}'
