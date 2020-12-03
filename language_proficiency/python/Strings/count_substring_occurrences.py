""" https://www.hackerrank.com/challenges/find-a-string/problem """
from collections import deque


def count_substring(s, sub_s):
    dq = deque()
    for i, c1 in enumerate(s):
        if c1 == sub_s[0] and len(s) - i >= len(sub_s):
            cnt = 0
            dq.append(i)
            for offset, c2 in enumerate(sub_s):
                if c2 == s[i + offset]:
                    cnt += 1
                else:
                    dq.pop()
                    break

    return len(dq)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
