#問題
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d

import heapq

N, M = map(int, input().split())

#隣接リストとしてグラフを作る
G = []
for _ in range(0, N):
    G.append([])

for _ in range(0, M):
    u, v, c = map(int, input().split())

    #uからvへと、重みcの辺が張られている為、行き先のvだけでなく重みのcも入れておく
    G[u].append((v, c))

#ダイクストラ法の実装
#頂点0から各頂点への最短距離を保持する配列
#N個の-1で満たしておく(-1の場合は未訪問である事を表す)
dist = []
for _ in range(0, N):
    dist.append(-1)

#ダイクストラ法で使うヒープ
Q = []

#始点となる頂点0をヒープに追加しておく
#(距離、頂点)として追加する
heapq.heappush(Q, (0, 0))

#始点となる頂点0への最短距離は0とする
dist[0] = 0

#ヒープから取り出した事があるかを保存する
#最初はN個のFalseで埋めておく
done = []
for _ in range(0, N):
    done.append(False)

#ダイクストラ法で各頂点への最短距離を求める
while len(Q) > 0:
    #ヒープの先頭の頂点を取り出してiとする
    d, i = heapq.heappop(Q)

    #もしヒープから取り出した事があれば、隣接する頂点を調べるのをスキップする
    if done[i]:
        continue

    #ヒープから頂点iを取り出したことを記録しておく
    done[i] = True

    #頂点iに隣接すつ頂点を順番に見る
    #見ている頂点をiとする
    #また、iからjへ移動する時に使う辺の重みをcとする
    for (j, c) in G[i]:

        #jが未訪問だった時、あるいはjへの最短距離が更新可能だった時。
        #jへの最短距離を更新して、ヒープの末尾に追加する
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N - 1])
