""" https://www.hackerrank.com/challenges/string-validators/problem """


def has_any(string):
    funcs = ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']

    for func in funcs:
        for idx, char in enumerate(string):
            if eval(f'\'{char}\'.{func}'):
                print('True')
                break
            elif idx == len(string) - 1:
                print('False')


if __name__ == '__main__':
    s = input()
    has_any(s)
