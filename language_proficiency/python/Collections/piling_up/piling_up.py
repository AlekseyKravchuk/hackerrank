""" https://www.hackerrank.com/challenges/piling-up/problem """

from collections import deque


def check_if_pile_possible(dq):
    while len(dq) > 2:
        if dq[0] >= dq[-1]:
            base = dq.popleft()
        else:
            base = dq.pop()

        if dq[0] > base or dq[-1] > base:
            return False

    return True


def print_wrapper(v):
    if v:
        print('Yes')
    else:
        print('No')


def main():
    sideLengths = []
    n_tests = int(input())
    for t in range(n_tests):
        _ = int(input())
        sideLengths.append(deque([int(length) for length in input().split()]))
    for dq in sideLengths:
        print_wrapper(check_if_pile_possible(dq))


if __name__ == '__main__':
    main()
