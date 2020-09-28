"""
 @author Cay Horstmann
 @author Modified by Paul Wolfgang
 @author Modified by Charles Wang
 @author Modified by Alexa Delacenserie
 @author Modified by Tarek Elseify
 @author Modified by Paul Hutchings
"""
from bank import Bank
import concurrent.futures as cf, random, threading

def transfer_thread(bank: Bank, from_account: int, max_amount: int):
    for i in range(10000):
        to_account = random.randint(0, bank.get_num_accounts() - 1)
        amount = random.randint(0, max_amount)
        bank.transfer(from_account, to_account, amount)
    print(f'Thread {threading.get_ident()} has finished with its transactions.')

if __name__ == "__main__":
    N_ACCOUNTS = 10
    INITIAL_BALANCE = 10000
    bank = Bank(N_ACCOUNTS, INITIAL_BALANCE)
    print('Bank transfer is in progress...')
    with cf.ThreadPoolExecutor(max_workers=N_ACCOUNTS) as executor:
        futures = []
        for i in range(N_ACCOUNTS):
            futures.append(executor.submit(transfer_thread, (bank, i, INITIAL_BALANCE)))
        cf.wait(futures)
        bank.test()