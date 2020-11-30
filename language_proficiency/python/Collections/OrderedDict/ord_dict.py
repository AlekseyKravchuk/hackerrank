""" https://www.hackerrank.com/challenges/py-collections-ordereddict/problem """

from collections import Counter
# from collections import OrderedDict


def main():
    lst = []
    for i in range(int(input())):
        line = input().split()
        item_name = ' '.join(line[:-1])
        price = int(line[-1])
        lst.append((item_name, price))
    cnt = Counter(lst)
    for key in cnt:
        print(f'{key[0]} {key[1] * cnt[key]}')

    # ######## Solution № 2 ########
    # ordered_dict = OrderedDict()
    # for tpl in lst:
    #     if tpl[0] in ordered_dict.keys():
    #         ordered_dict[tpl[0]] += tpl[1]
    #     else:
    #         ordered_dict[tpl[0]] = tpl[1]
    #
    # for key, value in ordered_dict.items():
    #     print(f'{key} {value}')


if __name__ == '__main__':
    main()
