def main():
    ans = 0
    n, m = map(int, input().split())  # 입력 받기
    trees = list(map(int, input().split()))  # 나무 높이 입력 받기

    trees.sort(reverse=True)  # 내림차순 정렬

    std = trees[0]  # 가장 높은 나무 높이를 시작점으로 설정
    k = 0  # 현재 처리하는 나무의 인덱스

    while k < len(trees) - 1:
        if ans >= m:
            print(std)
            return
        if (trees[k] - trees[k + 1]) * (k + 1) >= m - ans:
            if (m - ans) % (k + 1) == 0:
                std -= (m - ans) // (k + 1)
            else:
                std -= (m - ans) // (k + 1) + 1
            ans = m
        else:
            ans += (trees[k] - trees[k + 1]) * (k + 1)
            std = trees[k + 1]
        k += 1

    if (m - ans) % (k + 1) == 0:
        std -= (m - ans) // (k + 1)
    else:
        std -= (m - ans) // (k + 1) + 1

    print(std)

if __name__ == "__main__":
    main()
