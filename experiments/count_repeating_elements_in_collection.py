# count of each name in a list of names given as

from collections import defaultdict

names_str = 'Mike, John, Mike, Anna, Mike, John, John, Mike, Mike, Britney, Smith, Anna, Smith'
names = [x for x in names_str.split(', ')]
print(names)

count = defaultdict(int)

for name in names:
    count[name] += 1

print(f'count.items() = {count.items()}, type(count.items()) = {type(count.items())}')
# print(f'dict items: {list(count.items())}')