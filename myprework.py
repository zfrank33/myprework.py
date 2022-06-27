# Question 1
# write a function to print"hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_"+user_name)
user_name = input('Enter USERNAME: ')
hello_name(user_name)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odd():
    for i in range (1101):
        if i % 2 ! =0:
            print(i)
first_odd()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
 maximum = a_list[0]
 for i in range(len(a_list)):
     if a_list[i] > maximum:
        maximum = a_list[i]
        return maximum
a_list = [10, 20, 30, 40, 50]
print(max_num_in_list(a_list))
      
# Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)

    # Function named is_leap_year that takes year as parameter and returns
# True if the year is leap year otherwise False
def is_leap_year(a_year):
    # Checking if the year is divisible ny 400
    if(a_year % 400 == 0):
        return True
    # Checking if the year is divisible 100. If it is divisible then it is
    # Not a leap year
    elif a_year % 100 == 0:
        return False
    # Checking if the year is divisible by 4.
    elif a_year%4 == 0:
        return True
    # Otherwise False
    else:
        return False
# Asking the user to enter year 
a_year = int(input())
# Calling function is_leap_year
print(is_leap_year(a_year))

# Question 5
# Write a funcion to see if all the numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
# Driver Code
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))