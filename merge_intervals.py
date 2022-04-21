intervals = [[1,3],
             [4,5],
             [5,7],
             [8,11],
             [9,10]
             ]
intervals.sort()
result = [intervals[0]]

for start, end in intervals[1:]:
    lastend = result[-1][1]
    if start <= lastend:
        result[-1][1] = max(end, lastend)
    else:
        result.append([start, end])

print(result)

