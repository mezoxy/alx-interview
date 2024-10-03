#!/usr/bin/python3
'''prime game'''


def isWinner(x, lst):
    '''isWinner: to determine the wimer'''
    roundsMria = 0
    roundsBen = 0
    start = 0
    count = 0

    if lst is None or lst == [] or x <= 0 or len(lst) != x:
        return None

    lst = sorted(lst)

    for number in range(1, lst[-1] + 1):
        if number <= lst[start] and isprime(number):
            count += 1
        if number > lst[start]:
            start += 1
            if count % 2 == 0:
                roundsBen += 1
            else:
                roundsMria += 1
            count = 0
    return 'Maria' if roundsMria > roundsBen else 'Ben'


def isprime(num):
    '''isprime: to determine if a number is prime or not'''
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return False
