""" https://www.hackerrank.com/challenges/collections-counter/problem """

from collections import Counter


def main():
    num_shoes = int(input())
    shoes_sizes = Counter(map(int, input().split()))
    num_customers = int(input())

    total = 0
    for i in range(num_customers):
        requested_size, price, *_ = list(map(int, input().split()))
        total += price * (shoes_sizes[requested_size] > 0)
        shoes_sizes[requested_size] -= 1
    print(total)


if __name__ == '__main__':
    main()
