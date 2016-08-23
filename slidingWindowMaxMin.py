N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
start = 0
end = start + K
min_diff = None
while end <= N:
    subList = list()
    
    subList = lists[start:end]
    diff = subList[K-1] - subList[0]
    if min_diff is None:
        min_diff = diff
    else:
        if diff < min_diff: 
            min_diff = diff
    start = start + 1
    end = start + K
print min_diff
