"""
 @author Cay Horstmann
 @author Modified by Paul Wolfgang
 @author Modified by Charles Wang
 @author Modified by Alexa Delacenserie
 @author Modified by Tarek Elseify
 @author Modified by Paul Hutchings
"""
import threading, random
from bank import Bank

class TransferThread:
    def __init__(self, bank: Bank, from_acc: int, max_amount: int):
        """
        Creates a new TransferThread
        """
        self._bank = bank
        self._from_account = from_acc
        self._max_amount = max_amount
        self._thread = threading.Thread(target=self._run)

    def start(self):
        """
        Starts the TransferThread
        """
        self._thread.start()
    
    def join(self):
        self._thread.join()

    def _run(self):
        """
        The function to run during Thread execution
        """
        for i in range(10000):
            to_account = random.randint(0, self._bank.get_num_accounts() - 1)
            amount = random.randint(0, self._max_amount)
            self._bank.transfer(self._from_account, to_account, amount)

        print(f'Thread {threading.get_ident()} has finished with its transactions.')