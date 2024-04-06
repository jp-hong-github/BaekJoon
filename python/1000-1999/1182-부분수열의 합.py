def dfs(_idx, _sum):
    global n, s, arr
    _num = 0  # 합이 s인 부분수열의 개수
    if _idx == n:  # arr 벗어남
        return 0
    if _sum + arr[_idx] == s:  # 이번 숫자를 더했을 때 s와 같다면
        _num += 1  # _num을 1 높임

    # 백트래킹
    _num += dfs(_idx + 1, _sum)  # 이번 숫자 포함 X
    _num += dfs(_idx + 1, _sum + arr[_idx])  # 이번 숫자 포함 O

    return _num  # 백트래킹을 통해 얻은 값을 리턴


n, s = map(int, input().split())  # 입력
arr = list(map(int, input().split()))  # 숫자 입력

print(dfs(0, 0))
