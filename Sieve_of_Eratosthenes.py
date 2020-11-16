''' This is an approach to solve the following:
Write a function find_primes(high) that prints all prime numbers less than high. Function should
fail/exit for invalid values of high.

This can be solved using Sieve of Eratosthenes:

    Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
    Initially, let p_num equal 2, the first prime number.
    Starting from p_num^2, count up in increments of p_num and mark each of these numbers greater than or equal to p^2 itself in the list. 
    These numbers will be p_num(p_num+1), p_num(p_num+2), p_num(p_num+3), etc..
    Find the first number greater than p_num in the list that is not marked.
    If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
'''

def sieve_of_Eratosthenes(num):
    non_prime_list = []
    for i in range(2, num):
        if i not in non_prime_list:
            print (i)
            for j in range(i*i, num+1, i):
                non_prime_list.append(j)
    

num = int(input("Enter the number") )
sieve_of_Eratosthenes(num)