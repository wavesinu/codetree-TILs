from itertools import permutations


k, n = tuple(map(int, input().split()))
nums = [i for i in range(1, k + 1)]

for i in permutations(nums, n):
    if all(i[j] != i[j+1] for j in range(n-1)):
        print(" ".join(map(str, i)))