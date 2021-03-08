#問題
#https://atcoder.jp/contests/abc157/tasks/abc157_b

#ビンゴカードを表す二次元配列となる予定の配列
A = []
for i in range(0, 3):
    #ビンゴカードの一行を受け取る
    #これは一次元配列となっている
    row = list(map(int, input().split()))

    #受け取った一行分の配列をAの末尾に追加する
    #Aは一次元配列を要素とする配列である為、Aは二次元配列である
    A.append(row)

#ビンゴカードの数字に印がついているかどうかを記録する為の配列
M = []
for i in range(0, 3):
    #一行分を表す一次元配列
    row = []
    for j in range(0, 3):
        row.append(False)
    
    M.append(row)

#実装
N = int(input())

#選ばれた数がビンゴカードに書かれているか確認する
for _ in range(0, N):
    #選ばれた数字
    b = int(input())

    #bがビンゴカードに書かれているか調べる
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                #もしビンゴカードのi行目j列目に数字bがあればM[i][j] = Trueとして印をつける
                M[i][j] = True

#ビンゴを達成しているかを記録する変数
bingo = False

for i in range(0, 3):
    #i行目の3つに印がついているか調べる
    #ついていたらビンゴ達成
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    #i列目の3つに印がついているか調べる
    #ついていたらビンゴ達成
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

#左上から右下にかけて、斜めに3つ印が付いているか調べる
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

#右上から左下にかけて、斜めに3つ印がついているか調べる
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

#ビンゴを達成していたらYes
if bingo:
    print("Yes")
else:
    print("No")
