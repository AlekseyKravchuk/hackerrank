""" https://www.hackerrank.com/challenges/swap-case/problem """


def swap_case(s):
    funcs = (lambda x: x.lower(), lambda x: x.upper())
    # new_s = ''.join([funcs[0](ch) if ch.isupper() else funcs[1](ch) for ch in s])
    return ''.join([funcs[ch.islower()](ch) for ch in s])


if __name__ == '__main__':
    print(swap_case(input()))
