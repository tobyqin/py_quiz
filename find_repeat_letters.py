"""
找出数字序列中重复多次的连续3个数字。
"""

input_string = 'abcabcaabbccabccabbccaabcc'

split = [input_string[x:x + 3] for x in range(len(input_string) - 2)]

counter = {}

for x in split:
    counter.setdefault(x, 0)
    counter[x] += 1

for k, v in counter.items():
    if v > 2:
        print('{} repeat {} times'.format(k, v))
