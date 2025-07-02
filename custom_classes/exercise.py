from datetime import datetime

class OverdraftNotAllowed(Exception):
    '''custom exception class'''

class Account:
    def __init__(self, first_name, last_name, account_number, balance, is_overdraft_allowed = False):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = balance
        self._is_overdraft_allowed = is_overdraft_allowed
        self._ledger = []

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def ledger(self):
        return self._ledger

    def add_to_ledger(self, entry):
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._ledger.append((dt, entry))

    @property
    def is_overdraft_allowed(self):
        return self._is_overdraft_allowed

    @is_overdraft_allowed.setter
    def is_overdraft_allowed(self, val):
        if isinstance(val, bool):
            self._is_overdraft_allowed = val
            return self._is_overdraft_allowed
        raise ValueError('is_overdraft_allowed only takes bool')

    def withdraw(self, val):
        if val < 0:
            raise ValueError('Must be a positive value')
        if (self._balance - val) < 0 and self._is_overdraft_allowed == False:
            raise OverdraftNotAllowed('not allowed to have negative balance')
        else:
            self.add_to_ledger(val)
            self._balance -= val
            return self._balance

    def __eq__(self, other):
        return isinstance(other,Account) and self._account_number == other._account_number




a = Account('Erik', 'Liljuros', 10, 500)
b = Account('Erik', 'Liljuros', 20, 500)
print(a == b)

