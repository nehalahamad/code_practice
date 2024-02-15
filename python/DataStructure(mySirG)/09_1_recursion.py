# https://www.youtube.com/watch?v=D00dMdaEU0U&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=28

'''
1 - Write a recursive function to print first N natural numbers.
2 - Write a recursive function to print first N natural numbers in reverse order.
3 - Write a recursive function to print first N odd natural numbers.
4 - Write a recursive function to print first N even natural numbers.
5 - Write a recursive function to print first N odd natural numbers in reverse order.
6 - Write a recursive function to print first N even natural numbers in reverse order.
'''
# 1
def print_n(n):
    if n > 0:
        print_n(n-1)
        print(n, end=' ')
# 2
def print_n_reverse(n):
    if n > 0:
        print(n, end=' ')
        print_n_reverse(n-1)
# 3
def print_n_odd(n):
    if n > 0:
        print_n_odd(n-1)
        print(2*n-1, end=' ')
# 4
def print_n_even(n):
    if n > 0:
        print_n_even(n-1)
        print(2*n, end=' ')
# 5
def print_n_odd_reverse(n):
    if n > 0:
        print(2*n-1, end=' ')
        print_n_odd_reverse(n-1)
# 6
def print_n_even_reverse(n):
    if n > 0:
        print(2*n, end=' ')
        print_n_even_reverse(n-1)


if __name__ == "__main__":
    # print_n(10)
    # print_n_reverse(10)
    # print_n_odd(10)
    # print_n_even(10)
    # print_n_odd_reverse(10)
    print_n_even_reverse(10)