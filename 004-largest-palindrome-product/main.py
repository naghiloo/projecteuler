# Largest Palindrome Product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer:  906609
# Completed on Sun, 24 Jan 2016, 14:06

digits = 8

def max_by_digits(digits):
    return 10**digits - 1

def is_palindrome(n):
    return n == int(str(n)[::-1])


result = [0, 0, 0]
loop_start_border = max_by_digits(digits)
loop_end_border = 10**(digits-1)

for i in range(loop_start_border, 1, -1):
    # print((((10**digits) - i)*100)/(10**digits), i, (i * loop_start_border) - result[2], result[2])
    if i * loop_start_border < result[2]:
        break
    
    for j in range(loop_start_border, loop_end_border//i, -1):
        product = i * j
        if product < result[2]:
            break

        if is_palindrome(product):
            loop_end_border = product
            result = [i, j, max(result[2], product)]
            break

print(result)

