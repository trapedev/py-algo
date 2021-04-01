import heapq
N = int(input())
G = []
#頂点iがマークされているかどうかを管理する配列
#頂点iがマークされている時 marked[i] = True
#最初はdの頂点もマークされていない為、False
marked = []
for _ in range(0, N):
    marked.append(False)

#マークされている頂点の数を保持する変数
#最初はどの頂点もマークされていない為 0
#この値がNになったら終了
marked_count = 0

#最初に頂点0を選んでマークする
marked[0] = True
marked_count += 1

#最初に選ぶ辺の候補を入れるヒープ
Q = []

#頂点0に隣接する編を調べヒープに入れる
for j, c in G[0]:
    #ヒープに選ぶ候補の辺を挿入する
    #(辺の重み、選んだ時にマークする頂点)の形式で保存
    heapq.heappush(Q, (c, j))

#最小全域木の重みの合計を保存する変数
sum = 0

#すべての頂点がマークされるまで繰り返す
while marked_count < N:
    #ヒープから、最小の重みの辺えお取り出す
    #これは(辺の重み、選んだ時にマークする頂点)の形式になっている
    c, i = heapq.heappop(Q)

    #辺につながる頂点iも既にマークされていた場合、
    #操作おｗスキップする
    if marked[i]:
        continue

    #頂点iをマークする
    marked[i] = True
    marked_count += 1

    #使った辺は最小全域木となる為、重みを保存しておく
    sum += c

    #新たにマークした頂点iに隣接する辺を調べる
    for (j, c) in G[i]:
        #辺がつなぐ頂点が既にマークされていた場合はヒープに入れない
        if marked[i]:
            continue

        heapq.heappush(Q, (c, j))

#最小全域木の重みの合計
print(sum)
