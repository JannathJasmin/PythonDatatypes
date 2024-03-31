# a.Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
# ((10 ** 2) / 2) + ((50 * 2) - 49.75)
# = (100 / 2) + (100 - 49.75)
# = 50 + 50.25
# = 100.25
result = ((10 ** 2) / 2) + ((50 * 2) - 49.75)
print(result)

# Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)=44  
#What is the value of the expression 4 * 6 + 5=29   
#What is the value of the expression 4 + 6 * 5=34 
result1 = 4 * (6 + 5)
result2 = 4 * 6 + 5
result3 = 4 + 6 * 5
print("Result of 4 * (6 + 5) is:", result1)
print("Result of 4 * 6 + 5 is:", result2)
print("Result of 4 + 6 * 5 is:", result3)

# What is the *type* of the result of the expression 3 + 1.5 + 4?
a=3+1.5+4
print(type(a))

# What would you use to find a number’s square root, as well as its square? 
number = 10
# Calculate square root
square_root = number ** 0.5
print("Square root of", number, "is:", square_root)

# Calculate square
square = number * number
print("Square of", number, "is:", square)


# String
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
char_e = s[1]
print(char_e)

# Reverse the string 'hello' using slicing:
s = 'hello'
rev_txt = s[::-1]
print(rev_txt)

# Write a program to detect double spaces in a string
# To add a space between string, add a " ":
a = "Hello"
b = "World"
c = a + " "+ b
print(c)

# Replace the double spaces from the above problem  with single spaces.
a = "Hello"
b = "World"
c = a + "  " + b  # Adding double space
# Replace double spaces with single spaces
c = c.replace("  ", " ")
print(c)


# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1: Positive indexing
s = 'hello'
pos_index = s[4]
print(pos_index)  

# Method 2: Negative indexing
s = 'hello'
pos_index = s[-1]
print(pos_index) 

# Write a program to fill name and date in the letter template given below
name = input("Enter recipient's name: ")
date = input("Enter today's date: ")
letter = """Dear {},
Greetings from ABC coding house. 
I am happy to tell you about your selection
You are selected!
Have a great day ahead!
            Thanks and regards,
                        Bill
Date: {}""".format(name, date)
print(letter)

# LIST
# Build this list [0,0,0] two separate ways.
list1=[0,0,0]
print(list1)

list2 = [0] * 3
print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)
# sorted list
list4 = [5,3,4,6,1]
list4.sort()
print(list4)


# dictionary
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
x=d['simple_key']
print(x)
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'k1':{'k2':'hello'}}
x=d['k1']['k2']
print(x)

#Grab hello
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
x=d['k1'][0]['nest_key'][1][0]
print(x)


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
x=d['k1'][2]['k2'][1]['tough'][2][0]
print(x)

# TUPLE
# How do you create a tuple?
t=("a","b","c")
print(t)

# SET
# Use a set to find the unique values of the list below
list5 = [1,2,2,33,4,4,11,22,3,3,2]
s=set(list5)
print(s)

# BOOLEAN
# 2 > 3
a=2
b=3
print(a>b)

# 3 <= 2
a=3
b=2
print(a<=b)

# 3 == 2.0
a=3
b=2.0
print(a==b)

# 3.0 == 3
a=3.0
b=3
print(a==b)

# 4**0.5 != 2
a=4**0.5
b=2
print(a!=b)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False? ans:false
print(l_one[2][0] >= l_two[2]['k1'])


