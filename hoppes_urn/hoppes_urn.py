import numpy as np


# 上昇階乗(Ascending Facorial)
def AF(a, n) :
    res = 1
    for i in range(n) :
        res *= a + i
    return res


# ホップの壺の試行に対する確率
def P(n_vec, *, a) :
    '''
    色玉がある組み合わせで壺に入れられる確率は，色玉の入れられた順序に依存しないことが確認できる
    '''

    n = len(n_vec)
    count_unique = np.zeros(len(set(n_vec)))
    for i in range(len(n_vec)) :
        if (i == 0) :
            res = a
        elif (n_vec[i] in n_vec[0:i]) :
            count_unique[n_vec[i]] += 1
            res *= count_unique[n_vec[i]]
        else :
            res *= a
    return res/AF(a,n)


# 順番を保持したまま重複削除
def uniqued(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


# ホップの壺の生成過程
def process(*, a, n) :
    '''
    黒玉の重さa(>0)，色玉の重さは全て1として，
    (1)最初はこの壺の中には黒玉が1個のみ入っている．
    (2)この壺から，玉の重さに比例した確率でランダムに玉を1個取り出す．
    (3)取り出した玉の色が黒のとき，そのときの壺の中にない色玉を無作為に選択し，
       取り出した黒玉と一緒に入れる．
    (4)取り出した玉が色玉のとき，その色と同じ色の色玉を，取り出した玉と一緒に
       壺に入れる．
    (5)n回繰り返し終わるまで上記2に戻る

    aの値が大きいほど，壺の中により多くの異なる種類の色玉が入れられ，
    逆にaの値が小さいほど，色玉の種類数が減少し，特定の(複数の)色玉の個数が増大しやすくなる
    '''
    seq = np.zeros(n)

    # 色玉は最大でn種類しか存在しない
    colors = list(range(n))
    count_colors = np.zeros(n)
    # n回試行する
    for m in range(n) :
        if (m == 0) :
            # 最初は黒玉を引くのでランダムに色玉を引いてカウントする
            pop_num = colors.pop(np.random.choice(colors))
            count_colors[pop_num] += 1
            seq[m] = pop_num
        else :
            # p_colorsの確率に従って色玉を引いてカウントする
            p = np.random.choice(n+1, p=p_colors)
            if (p == n) :
                # 黒玉を引いたので引いていない色玉からランダムに色玉を引いてカウントする
                pop_num = colors.pop(colors.index(np.random.choice(colors)))
                count_colors[pop_num] += 1
                seq[m] = pop_num
            else :
                # 黒玉以外を引いたので，その玉を更に追加
                count_colors[p] +=1
                seq[m] = p

        # 第i色の色玉が選ばれる確率リストを計算する
        ## m回目に試行するとき，既に(m-1)個の色玉が入っている
        ## 第i色の色玉は現時点でcount_colors[i]個入っている
        p_colors = []
        p_colors.extend(count_colors/(m+1+a))
        p_colors.append(a/(m+1+a))
    return seq


# イーウェンスの抽出公式
def P_E(n_vec, *, a) :
    n_vec = list(n_vec)
    len_n = len(n_vec)
    print(n_vec)
    if (0 in n_vec) :
        print(n_vec)
        # n_vec.remove(0)
    else :
        print("a")
    c = len(n_vec)
    p = 0

    if (len_n != c) :
        n_vec = np.array(n_vec)
        p = np.math.pow(a,c)*np.math.factorial(sum(n-1))
    return p
