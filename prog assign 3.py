#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[10]:


num = float(input("Enter a number: "))  
if num > 0:  
    print("{0} is a positive number".format(num))  
elif num == 0:  
    print("{0} is zero".format(num))   
else:  
    print("{0} is negative number".format(num))   


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[23]:


num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  


# 3. Write a Python Program to Check Leap Year?

# In[8]:


year = int(input("Enter a year: "))  
if (year%4) == 0:
    print(format(year),"is a leap year")    
else:
    print(format(year),"is not a leap year")


# 4. Write a Python Program to Check Prime Number?

# In[22]:


#python programme to check number is prime number or not

num = int(input("Enter a number: "))   
for i in range(2,num):  
    if num%i == 0:  
        print(num,"is not a prime number")
    break
else:  
    print(num,"is a prime number")  


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[28]:


minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

Number = minimum

while(Number <= maximum):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1


# In[ ]:




