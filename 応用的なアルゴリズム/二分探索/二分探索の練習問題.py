#問題
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ok = N
ng = -1

while abs(ok - ng) > 1:
    mid = (ok + ng) //2

    if A[mid] >= K:
        ok = mid
    else:
        ng = mid

#条件を満たす要素が存在しない場合はokが初期値のままになる為、-1を出力
if ok == N:
    print(-1)
else:
    print(ok)

