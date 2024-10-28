#!/usr/bin/env python
# coding: utf-8

# ### Objects

# We'll cover this later in this course, but let me first show you how we can create custom objects with state and functionality.
# 
# So, don't worry if you don't understand this code right now, you soon will!

# In[1]:


class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance
        
    def deposit(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0:
            self.balance = self.balance + amount
            print(f'Deposited {amount}')
            print(f'New balance is: {self.balance}')
        else:
            print(f'{amount} is an invalid amount.')
            
    def withdraw(self, amount):
        # should also check that amount is a numerical value!
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Withdrawal: {amount}')
            print(f'New Balance: {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount')
            else:
                print('Insufficient funds.')
                print(f'Current balance is {self.balance}')


# In[2]:


my_account = Account('123-456', 'savings', 1_000.00)


# `my_account` is an **object** with **state**:

# In[3]:


my_account.account_number


# In[4]:


my_account.account_type


# In[5]:


my_account.balance


# And it has **functionality**:

# In[6]:


my_account.deposit(100)


# In[7]:


my_account.withdraw(600)


# In[8]:


my_account.withdraw(10_000)


# As you can see we can access state and functionality of objects using this **dot** notation.

# In Python, everything is an object - this means everything we work with has state and functionality.

# For example, integers are objects - they have **state** (their value), as well as **functionality** (they know how to add another number to themselves):

# In[9]:


10 + 15


# The `+` operator is actually using a functional attribute of the integer, called `__add__`.

# We could have done the addition this way:

# In[10]:


(10).__add__(15)


# In the same way, `floats` are also objects:

# In[11]:


0.125


# One piece of functionality they have is the `as_integer_ratio` method, which can be useful if you want to get an exact representation of the float:

# In[12]:


(0.125).as_integer_ratio()


# As you can see `0.125` is stored **exactly** as `1/8`.

# But as we know, not every float literal we specify can be stored exactly as we wrote it:

# In[13]:


0.1


# This may look like Python is storing this as `0.1`, but we know better:

# In[14]:


format(0.1, '.25f')


# But what is the **exact** number?

# In[15]:


(0.1).as_integer_ratio()


# As we can see it is some big fraction, very close to `1`, but not exactly `1`.

# We'll come back to these kinds of topics, but for now the main take away is that everything we work with in Python is an object.
