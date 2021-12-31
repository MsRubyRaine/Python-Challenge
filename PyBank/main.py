#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


budget_data=os.path.join('Resources','budget_data.csv')


# In[22]:


with open(budget_data, 'r') as csvfile:
    budgetcsv = csv.reader(csvfile,delimiter=',')
    
    NoOfRows=[]
    
    for row in budgetcsv:
            
        NoOfRows.append(row)
    NoOfRows.pop(0)


# In[32]:


y=0

for row in NoOfRows:
    y=y +int(row[1])


# In[49]:


index=0
ChangeList = []

for profit in NoOfRows:
    # Get current and last profit
    CurrentProf=profit[1]
    LastProf=NoOfRows[index-1][1]
    
    # Calculate change
    change = (int(CurrentProf) - int(LastProf))
    
    # Add change to the ChangeList
    ChangeList.append(change)
    
    index+=1


ChangeList.pop(0)

AverageChange = round(sum(ChangeList) / len(ChangeList),2)


# In[60]:


BigChange = ChangeList.index(max(ChangeList))

#Go to NoOfRows -> Go to Row # that we got from BigChange + 1, to account for the 
#popped line. Then 0 is the first coloumn that we want the answer from.

BigChange1 = ChangeList.index(min(ChangeList))


# In[74]:


print("Financial Analysis")
print("----------------------------")
print("Total Months:"+ str(len(NoOfRows)))
print("Total: $"+str(y))
print("Average Change: $"+str(AverageChange))
print("Greatest Increase in Profits:"+ str(NoOfRows[BigChange+1][0])+" ($"+str(max(ChangeList))+")")
print("Greatest Decrease in Profits:"+ str(NoOfRows[BigChange1+1][0])+" ($"+str(min(ChangeList))+")")


# In[ ]:




