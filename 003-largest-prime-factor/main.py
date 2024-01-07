# Largest Prime Factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#
# Answer:  6857
# Completed on Thu, 14 Jan 2016, 15:57

number = 600851475143

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

for i in range(int(number**0.5)+1, 3, -1):
    if number % i == 0 and is_prime(i):
        print(i)
        break
