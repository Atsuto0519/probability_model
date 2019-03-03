import numpy as np
import hoppes_urn

# 試行回数
a = 5
print("a="+str(a))

# 試行に伴って対応する色系列(色の並びに決まりはない)
x_1 = list("赤黄黄赤赤緑")
x_2 = list("緑黄黄赤赤赤")
n = len(x_1)
print("n="+str(n))
print("２つの入力が同じ確率で表されることを確認する")
print("input x_1="+str(x_1))
print("input x_2="+str(x_2))

# 色に対して，第i色目であることを紐付ける
x_1_unique = hoppes_urn.uniqued(x_1)
x_2_unique = hoppes_urn.uniqued(x_2)
x_1_index = [x_1_unique.index(i) for i in x_1]
x_2_index = [x_2_unique.index(i) for i in x_2]
print("processed x_1="+str(x_1_index))
print("processed x_2="+str(x_2_index))

# 最終的なホップの壺の計算結果
print("x_1 processed Hoppe's urn model="+str(hoppes_urn.P(x_1_index, a=a)))
print("x_2 processed Hoppe's urn model="+str(hoppes_urn.P(x_2_index, a=a)))
