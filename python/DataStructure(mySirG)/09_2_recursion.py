# https://www.youtube.com/watch?v=WLhw-d9l6h4&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=29
'''
1 - Write a recursive function to calculate sum of first N natural numbers.
2 - Write a recursive function to calculate sum of first N odd natural numbers.
3 - Write a recursive function to calculate sum of first N even natural numbers.
4 - Write a recursive function to calculate factorial of a numbers.
5 - Write a recursive function to calculate sum of squares of first N natural numbers.
'''
# 1
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)
# 2 
def sum_n_odd(n):
    if n == 1:
        return 1
    return (2*n-1) + sum_n_odd(n-1)
# 3
def sum_n_even(n):
    if n == 1:
        return 2
    return 2*n + sum_n_even(n-1)
# 4
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
# 5
def sum_square_n(n):
    if n == 1:
        return 1
    return n*n + sum_square_n(n-1)


if __name__ == "__main__":
    # print(sum_n(5))
    # print(sum_n_odd(3))
    # print(sum_n_even(3))
    # print(factorial(5))
    print(sum_square_n(3))