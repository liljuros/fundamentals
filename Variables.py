#!/usr/bin/env python
# coding: utf-8

# ### Variables

# Recall that we use the `=` symbol as the **assignment** operator. 

# We specify a variable name (a label) on the left hand side of the operator, and the value (or expression that evaluates to a value) on the right hand side.

# In[1]:


a = 100


# Now `a` is a symbol (a variable) in our program that we can recall:

# In[2]:


a


# We can use it in subsequent parts of our code:

# In[3]:


b = a + 11


# In[4]:


b


# As you can see, here we performed a calculation in the right hand side, and assigned that resulting value to the label on the left (`b`).

# Note that the `=` symbol is not the same as the mathematical *equality* symbol, so something like this is not valid Python, and we'll get an exception:

# In[5]:


10 = 10


# Note also that the object the symbol `a` or `b` points to can change over time:

# In[6]:


a


# In[7]:


a = 3.14


# In[8]:


a


# As you can see, `a` used to reference the integer `100`, but now it references a different object, the float `3.14`.

# #### Naming Rules

# As discussed in the lecture, there are certain rules you must follow when choosing variable names.
# 
# For example, all the following are valid variable names:

# In[9]:


test = 10
test_1 = 10
_test_1_ = 10
__test__ = 10
TEST = 10


# But a variable name may not start with a digit:

# In[10]:


1_test = 10


# And we should not use reserved keywords or built-in functions.

# For example, `if` is a reserved keyword:

# In[11]:


if = 10


# There are other symbols that Python has pre-defined for us and although we can change them, we should not.

# For example, `float` is used by Python to represent the float data type.

# In fact, we can create a float this way:

# In[12]:


a = float(10)


# In[13]:


a


# But, we *could* remap the symbol `float` to be something else:

# In[14]:


float = 100.5


# The problem now is that the original definition of `float` has been lost to us (internally Python still has it, but **we** don't!)

# In[15]:


a = float(10)


# Since I don't want to "overwrite" Python's symbol for `float`, I am going to delete that symbol I created:

# In[16]:


del float


# Now **my** definition of `float` is gone, and the **original** one provided by Python is available again.

# In[17]:


a = float(10)
print(a)


# #### Naming Conventions

# Python developers typically follow a standard naming convention for variable names. Depending on the type of variable, there are different conventions.

# In particular, we follow the PEP8 conventions:
# 
# https://www.python.org/dev/peps/pep-0008/

# You should try reading this guide once in a while (not all in one sitting, but just here and there as time permits - it's quite useful).

# For now, we are dealing with simple variables in our code, so we follow the snake case convention, with all letters lower cased:

# In[18]:


current_balance = 100.0


# and not, camel casing like in other languages such as Java or Javascript:

# In[19]:


currentBalance = 100.0


# The other advice I would give is to **always** give your variables meaningful names - not because the computer cares, but because humans reading your code (including yourself six months after you wrote that code) will find it easier to understand what's going on.

# Here's an example. Suppose I show you this piece of code, and ask you what does it do:

# In[20]:


x = 100
y = 0.1
z = 10

r = x * ((1 + y/12) ** (z * 12))

print(r)


# How about this code instead, which is identical, except for variable names:

# In[21]:


principal = 100
apr = 0.1
years = 10

future_value = principal * ((1 + apr/12) ** (years * 12))

print(future_value)

