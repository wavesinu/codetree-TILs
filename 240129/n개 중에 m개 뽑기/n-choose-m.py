def combination(n, m):
    answer = []

    def print_combination():
        for num in answer:
            print(num, end=" ")
        print()

    def find_combinations(current_num, cnt):
        if cnt == m:
            print_combination()
            return

        for num in range(current_num + 1, n + 1):
            answer.append(num)
            find_combinations(num, cnt + 1)
            answer.pop()

    find_combinations(0, 0)


m, n = tuple(map(int, input().split()))

# 함수 호출
combination(m, n)