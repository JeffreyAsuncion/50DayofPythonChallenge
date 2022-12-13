"""
Extra Challenge: List of Prime Numbers
Write a function called prime_numbers. This function asks a 
user to enter a number (integer) as an argument and returns a 
list of all the prime numbers within its range. For example, if user 
enters 10, your code should return [2, 3, 5, 7] as prime numbers.
"""

def isPrime(n):
    # base case
    if (n==1 or n==0):
        return False

    # Run a loop from 2 to n-1
    for i in range(2,n):
        if(n%i==0):
            return False
    
    # otherwise, n is prime number
    return True

def print_prime_list(num):
    
    prime_list = []
    for i in range(1,num+1):
        if isPrime(i):
            prime_list.append(i)
    
    return prime_list

num = 10
print(print_prime_list(num))