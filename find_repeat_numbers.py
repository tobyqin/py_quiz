"""
找出数字序列中重复多次的连续3个数字。
"""
number = '1233223332321234323123'

split = [number[position:position + 3] for position in range(len(number) - 2)]

seq = [0] * 1000

for x in split:
    seq[int(x)] += 1

for i in range(1000):
    if seq[i] > 1:
        print('{} repeat {} times'.format(i, seq[i]))
