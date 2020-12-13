import math
import os
import sys


def price(day: int) -> int:
    if day < 1:
        return 0
    if day == 1:
        return 1
    day -= 1
    x = int(math.sqrt(day * 2))
    n = x * (x + 1) // 2
    current = 1 + (x - 1) * x // 2
    if n == day:
        return current
    else:
        return current + day - n


def main():
    for line in stdin:
        for var in line.split():
            n = int(var)
            print(price(n))


if __name__ == '__main__':
    stdin = sys.stdin
    if os.getenv('MODE') == 'debug':
        stdin = open('main.in')
    main()
    exit(0)
