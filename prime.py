''' This is an approach to solve the following Question in Python:
Write a function check_prime(num) to check if an integer is prime.
'''

def prime_check(num):
    i = 2
    while( i < (num/2) ):
        if( num%i != 0):
            flag_is_prime = True
            pass
        else:
            flag_is_prime = False
            break
        i += 1
    if ( flag_is_prime == False ):
        print( num,"is not a Prime Number" )
    else:
        print( num,"is a Prime Number" )
    return

number = int( input("Enter an Integer to check if it is Prime") )
ret = prime_check(number)
if ( ret != None):
    print(ret)