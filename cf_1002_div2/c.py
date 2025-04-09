arr = [[1,2,5,4,8],[12,7,3,4,8],[9,2,15,4,6],[2,2,5,14,18],[3,3,5,9,7]]
arr1 = [[] for _ in range(len(arr))]  # Correct initialization
for i in range(len(arr)):
    s = sum(arr[i])
    for j in range(len(arr[i])):
        s -= arr[i][j]
        arr1[i].append(s)
print(arr1)

def max_mex(arr1):
    n = len(arr1)
    for k in range(n+1):            # try MEX = k
        used = [False]*n            # which queues are already assigned
        ok = True
        for v in range(k):          # we need to produce value = v
            target_time_index = n - v - 1
            # find some queue i not used yet with arr1[i][target_time_index] == v
            found = False
            for i in range(n):
                if (not used[i]) and arr1[i][target_time_index] == v:
                    used[i] = True
                    found = True
                    break
            if not found:
                ok = False
                break
        if not ok:
            return k               # k is the first we cannot achieve
    return n

print(max_mex(arr1))