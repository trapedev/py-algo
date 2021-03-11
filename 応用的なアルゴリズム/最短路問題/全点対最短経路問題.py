#問題
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e

#∞を表す定数を用意
INF = 1_000_000_000_000_000_000

N, M = map(int, input().split())

#全ての頂点について最短経路を保持する配列を用意
dist = []

#最初は辺が一本も張られていない為、∞の辺が張られているとして、N×N個のINFで埋めておく
for i in range(0, N):
    dist.append([])
    for j in range(0, N):
        dist[i].append(INF)

#グラフの辺を受け取り,distに直接書き込む
for _ in range(0, M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

#iからiへの同じ頂点動詞の距離は0としておく
for i in range(0, N):
    dist[i][i] = 0

#ワーシャルフロイド法の実装
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

#全ての頂点の組について最短距離を合計
ans = 0
for i in range(0, N):
    for j in range(0, N):
        ans += dist[i][j]

print(ans)