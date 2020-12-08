""" https://www.hackerrank.com/challenges/designer-door-mat/problem """
from math import floor


def get_lines(N, M):
    lines = []
    for i in range(floor(N / 2)):
        hyphen_pad = '-' * (int((M - 3) / 2) - 3 * i)
        start = '.|'
        padding = '..|' * 2 * i
        end = '.'

        lines.append(hyphen_pad + start + padding + end + hyphen_pad)

    w = '-' * (int((M - 7) / 2)) + 'WELCOME' + '-' * (int((M - 7) / 2))

    lines.append(w)
    lines.extend(lines[len(lines) - 2::-1])
    return lines


if __name__ == '__main__':
    N, M = [int(val) for val in input().split()]
    for line in get_lines(N, M):
        print(line)
