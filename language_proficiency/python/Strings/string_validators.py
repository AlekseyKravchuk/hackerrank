""" https://www.hackerrank.com/challenges/string-validators/problem """

if __name__ == '__main__':
    s = input()
    funcs = [lambda x: x.isalnum(),
             lambda x: x.isalpha(),
             lambda x: x.isdigit(),
             lambda x: x.islower(),
             lambda x: x.isupper()]
    for f in funcs:
        print(bool(sum(map(f, s))))
        # print('True' if sum(map(f, string)) else 'False')
