""" https://www.hackerrank.com/challenges/collections-counter/problem """

from collections import Counter


def main():
    num_shoes = int(input())
    sizes = Counter([int(x) for x in input().strip().split()][:num_shoes])
    total_earn = 0

    for i in range(int(input())):
        I = input().split()
        unit = int(I[0])
        price = int(I[1])

        if sizes[unit] > 0:
            sizes[unit] -= 1
            total_earn += price

    print(total_earn)


if __name__ == '__main__':
    main()
