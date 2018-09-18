from collections import defaultdict

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = defaultdict(int)  # 使用lambda来定义简单的函数

for s in strings:
    counts[s] += 1

print(counts)