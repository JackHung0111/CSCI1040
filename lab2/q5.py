# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab2 Q5

def get_prime_numbers(n):
    primes = []
    for num in range(2, n):
        #TODO: Check if num is prime by looping over the primes list
        flag = 0
        for i in range(2, num):
            if(num % i == 0):
                flag = 1
        if(flag == 0):
            primes.append(num)
    return primes


#TODO: Handle console input and output
n = int(input("Enter a number: "))
print(get_prime_numbers(n), "are prime numbers smaller than " + str(n) + ".")