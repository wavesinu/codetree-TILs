import sys


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# print(arr)
#  n* n 격자를 벗어나지 않으면서, 3*3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 출력

# 3x3 격자의 최대 합을 저장할 변수
max_sum = 0

# 모든 가능한 3x3 격자를 순회
for i in range(n-2):
    for j in range(n-2):
        # 현재 3x3 격자의 합을 계산
        current_sum = sum(arr[i+k][j+l] for k in range(3) for l in range(3))
        # 최대 합을 갱신
        max_sum = max(max_sum, current_sum)

# 최대 합을 출력
print(max_sum)