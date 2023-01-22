#!/usr/bin/env python
# coding: utf-8

# In[74]:


class bankAccount():
    def __init__(self,name,money):
        self.name = name
        self.money = money 
    def add_money(self,amount):
        self.money = self.money + amount

        print ('{} added to your account'.format(amount))
    def withdrow(self,amount2):
        if (self.money >= amount2):
            self.money = self.money - amount2
            print ('{} withdrowed from your account'.format(amount2))
        else:
            print ('you have no sufficiant amount in your account to withdrow {} Eur'.format(amount2))
    def __str__ (self):
        return f"Account owner's name is {self.name}, current balance is {self.money}"
        


# In[75]:


my_account = bankAccount('Fatih', 100000)


# In[76]:


my_account.add_money(10000)


# In[77]:


print(my_account)


# In[78]:


my_account.withdrow(120000)


# In[79]:


print(my_account)


# In[80]:


my_account.withdrow(50000)


# In[81]:


print(my_account)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




