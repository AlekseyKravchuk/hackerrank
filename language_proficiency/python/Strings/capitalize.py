""" https://www.hackerrank.com/challenges/capitalize/problem """
import re


# hello          world  lol
# Hello World Lol


def is_not_blank(s):
    t = s.strip()
    temp = s and t
    res = bool(temp)
    return res


def solve(s):
    tokens = re.split(r'(\s+)', s)  # \s stands for “whitespace character”.
    for i, token in enumerate(tokens):
        if is_not_blank(token):
            if token.isalpha() and token[0].islower():
                tokens[i] = token.capitalize()

    return ''.join(tokens)


def main():
    s = input()
    print(solve(s))


if __name__ == '__main__':
    main()
