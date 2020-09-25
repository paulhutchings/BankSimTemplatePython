"""
 @author Cay Horstmann
 @author Modified by Paul Wolfgang
 @author Modified by Charles Wang
 @author Modified by Alexa Delacenserie
 @author Modified by Tarek Elseify
 @author Modified by Paul Hutchings
"""

from transfer_thread import TransferThread
from bank import Bank

if __name__ == 'main':
    N_ACCOUNTS = 10
    INITIAL_BALANCE = 10000

    bank = Bank(N_ACCOUNTS, INITIAL_BALANCE)
    threads = [TransferThread(bank, i, INITIAL_BALANCE) for i in range(N_ACCOUNTS)]
    print('Bank transfer is in progress...')
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    bank.test()
