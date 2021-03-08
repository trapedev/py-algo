#問題
#https://atcoder.jp/contests/past202005-open/tasks/past202005_e

N, M, Q = map(int, input().split())

#FalseのN×Nの2次元行列を作る
graph = []
for i in range(0, N):
    #長さがNのFalseの一次元行列を作る
    row = []
    for j in range(0, N):
        row.append(False)

    #長さNのFalseの一次元行列をgraphに追加する
    graph.append(row)

#M本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())

    #頂点番号は全て-1
    u -= 1
    v -= 1

    #uとvの間には辺があるためTrueにする
    graph[u][v] = True
    graph[v][u] = True

#頂点の色のリストを受け取る
C = list(map(int, input().split()))

#Q個のクエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    #スプリンクラーを起動するクエリの場合
    if query[0] == 1:
        x = query[1]

        #頂点番号は全て-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #全ての頂点を順番にみる
        for i in range(0, N):
            #頂点iが頂点xに隣接している時、すなわち頂点xと頂点iの間に辺がある時
            if graph[x][i]:
                #頂点iの色をC[x]に書き換える
                C[i] = C[x]

    #スプリンクラーを起動しないクエリの場合
    if query[0] == 2:
        x = query[1]
        y = query[2]

        #頂点番号は全て-1
        x -= 1

        #頂点xの色を出力する
        print(C[x])

        #頂点の色をyに書き換える
        C[x] = y