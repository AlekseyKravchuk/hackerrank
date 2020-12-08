""" https://www.hackerrank.com/challenges/text-wrap/problem """

import textwrap


def wrap(s, max_width):
    return '\n'.join(textwrap.wrap(s, max_width))


if __name__ == '__main__':
    s, max_width = input(), int(input())
    result = wrap(s, max_width)
    print(result)
