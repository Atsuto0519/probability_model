from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
import numpy as np
import hoppes_urn
import copy


def urn(x) :
    if (0.2<x and x<0.8) :
        return 0
    else :
        return 0.6

def my_index(ls, x, default=False):
    for l in ls :
        if (x == l[1]) :
            return ls.index(l)

# 試行回数とa
a = 3
n = 6
print("a="+str(a))
print("n="+str(n))

seq_colorball = np.zeros(n)

# 色玉は最大でn種類しか存在しない
colors = list(range(n))
count_colors = np.zeros(n)

colorball_p =[]
# n回試行する
for m in range(n) :
    randx = np.random.rand()*0.4+0.3
    randy = np.random.rand()*0.4+0.2
    if (m == 0) :
        # 最初は黒玉を引くのでランダムに色玉を引いてカウントする
        pop_num = colors.pop(np.random.choice(colors))
        count_colors[pop_num] += 1
        seq_colorball[m] = pop_num
        for phase in range(3) :
            plt.figure(figsize=(8, 8))
            ax = plt.gca()
            plt.ylim(0,1)
            plt.xlim(0,1)
            x_list = np.linspace(0, 1, 20)
            y_list = [urn(i) for i in x_list]
            plt.plot(x_list, y_list, "blue")
            if (phase == 0) :
                ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                ax.add_patch(ball)
            elif (phase == 1) :
                ball = Ellipse(xy=(0.5, 0.8), height=0.1, width=0.1, facecolor='k')
                ax.add_patch(ball)
                ball = Ellipse(xy=(0.6, 0.8), height=0.1, width=0.1, color=cm.hsv(pop_num/n))
                ax.add_patch(ball)
            else :
                ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                ax.add_patch(ball)
                colorball_p.append([[randx, randy], pop_num])
                for colorball in colorball_p :
                    ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                    ax.add_patch(ball)
            ## グラフ描画
            plt.draw()
            ## 更新待機（秒）
            plt.pause(1)

    else :
        # p_colorsの確率に従って色玉を引いてカウントする
        p = np.random.choice(n+1, p=p_colors)
        if (p == n) :
            # 黒玉を引いたので引いていない色玉からランダムに色玉を引いてカウントする
            pop_num = colors.pop(colors.index(np.random.choice(colors)))
            count_colors[pop_num] += 1
            seq_colorball[m] = pop_num
            for phase in range(3) :
                plt.figure(figsize=(8, 8))
                ax = plt.gca()
                plt.ylim(0,1)
                plt.xlim(0,1)
                x_list = np.linspace(0, 1, 20)
                y_list = [urn(i) for i in x_list]
                plt.plot(x_list, y_list, "blue")
                if (phase == 0) :
                    ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                elif (phase == 1) :
                    ball = Ellipse(xy=(0.5, 0.8), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    ball = Ellipse(xy=(0.6, 0.8), height=0.1, width=0.1, color=cm.hsv(pop_num/n))
                    ax.add_patch(ball)
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                else :
                    ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    colorball_p.append([[randx, randy], pop_num])
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                ## グラフ描画
                plt.draw()
                ## 更新待機（秒）
                plt.pause(1)
        else :
            # 黒玉以外を引いたので，その玉を更に追加
            count_colors[p] += 1
            seq_colorball[m] = p
            for phase in range(3) :
                plt.figure(figsize=(8, 8))
                ax = plt.gca()
                plt.ylim(0,1)
                plt.xlim(0,1)
                x_list = np.linspace(0, 1, 20)
                y_list = [urn(i) for i in x_list]
                plt.plot(x_list, y_list, "blue")
                if (phase == 0) :
                    pop_colorball = colorball_p.pop(my_index(colorball_p, p))
                    ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                elif (phase == 1) :
                    ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    ball = Ellipse(xy=(0.5, 0.8), height=0.1, width=0.1, color=cm.hsv(pop_colorball[1]/n))
                    ax.add_patch(ball)
                    ball = Ellipse(xy=(0.6, 0.8), height=0.1, width=0.1, color=cm.hsv(pop_colorball[1]/n))
                    ax.add_patch(ball)
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                else :
                    ball = Ellipse(xy=(0.5, 0.05), height=0.1, width=0.1, facecolor='k')
                    ax.add_patch(ball)
                    colorball_p.append([[randx, randy], pop_colorball[1]])
                    colorball_p.append([[randx+0.1, randy], pop_colorball[1]])
                    for colorball in colorball_p :
                        ball = Ellipse(xy=colorball[0], height=0.1, width=0.1, color=cm.hsv(colorball[1]/n))
                        ax.add_patch(ball)
                ## グラフ描画
                plt.draw()
                ## 更新待機（秒）
                plt.pause(1)

    # 第i色の色玉が選ばれる確率リストを計算する
    ## m回目に試行するとき，既に(m-1)個の色玉が入っている
    ## 第i色の色玉は現時点でcount_colors[i]個入っている
    p_colors = []
    p_colors.extend(count_colors/(m+1+a))
    p_colors.append(a/(m+1+a))


# ホップの壺モデルで色玉系列を作成する
print("colorball sequence:"+str(seq_colorball))

# 色玉系列を連番形式に変更
seq_colorball_unique = hoppes_urn.uniqued(seq_colorball)
seq_colorball_index = [seq_colorball_unique.index(i) for i in seq_colorball]
print("processed colorball="+str(seq_colorball_index))

# 最終的なホップの壺の計算結果
print("P(colorball)="+str(hoppes_urn.P(seq_colorball_index, a=a, n=n)))

# 最終的な結果を保存
plt.savefig('hoppes_urn/final_urn.png')
# グラフを閉じる
plt.close()
