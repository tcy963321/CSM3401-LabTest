#!/usr/bin/env python
# coding: utf-8

# In[26]:


def deciToBin(n):
    if(n != 0):
        return bin(n)[2:].zfill(8)
    else:
        print("Enter a number please!")

userInput = input("Enter a number in decimal: ")
i = deciToBin(int(userInput))
print("There are "+ str(i.count('1')) + " '1' in " + i)


# In[63]:


string = "I have Python exam"

def count():
    return len(string.split(' '))
print("There are "+str(count())+" words in sentences.")


# In[71]:


class MyString:
    def __init__(self, myString):
        self.__myString = myString

    def countWord(self):
         count = len(self.__myString.split())
         return count

    def findMostFrequentChar(self):        
        d = {}

        for ch in self.__myString.replace(' ', '').lower():
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        most_frequent = max(d, key=d.get)
        return most_frequent, d[most_frequent]


def main():    
    aString = MyString("an apple is not a tomato")
    print("There are", aString.countWord(), "words in the string.")

    letter, count = aString.findMostFrequentChar()
    print("The most frequent character is", letter, "which appeared", count, "times")

main()


# In[88]:


def multiply_by_two(x):
    return x*2

def add_number(a,b):
    return a+b
def print_arguments(args):
    print (f'Arguments are:{args}')

augmented_multiply_by_two = print_arguments(multiply_by_two(10))
x=augmented_multiply_by_two

augmented_add_number = print_arguments(add_number(3,4))
x=augmented_add_number


# In[94]:


def multiply_by_three(x):
    return x*3

def multiply_output(ambt):
    return 2*ambt

def print_arguments(args):
    print (f'Arguments are:{args}')
    
augmented_multiply_by_three = (multiply_by_three(10))
x=augmented_multiply_by_three
augmented_output=print_arguments(multiply_output(x))
ambt=augmented_output


# In[96]:


def add_numbers(a, b):
    return a+b

def multiply_output(addnum):
    return 2*addnum

def print_arguments(args):
    print (f'Arguments are:{args}')
    
augmented_add_number = (add_numbers(3,4))
x=augmented_add_number
augmented_output=print_arguments(multiply_output(x))
ambt=augmented_output


# In[ ]:




