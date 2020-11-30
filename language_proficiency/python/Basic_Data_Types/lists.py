""" https://www.hackerrank.com/challenges/python-lists/problem """


def main():
    lst = []
    for i in range(int(input())):
        command, *args = input().split()
        args = ', '.join(args)
        if args:
            exec(f'lst.{command}({args})')
        else:
            if command == 'print':
                exec('print(lst)')
            else:
                exec(f'lst.{command}()')


if __name__ == '__main__':
    main()
