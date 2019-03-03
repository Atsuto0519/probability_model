import numpy as np
import matplotlib.pyplot as plt
import hoppes_urn

# 試行回数とa
a = 5
n = 6
print("a="+str(a))

# ホップの壺モデルで色玉系列を作成する
seq_colorball = hoppes_urn.process(a=a, n=n)
print("colorball sequence:"+str(seq_colorball))
print("n="+str(n))

# 色玉系列を連番形式に変更
seq_colorball_unique = hoppes_urn.uniqued(seq_colorball)
seq_colorball_index = [seq_colorball_unique.index(i) for i in seq_colorball]
print("processed colorball="+str(seq_colorball_index))

# 最終的なホップの壺の計算結果
print("P(colorball)="+str(hoppes_urn.P(seq_colorball_index, a=a)))

# 確率が色玉系列の順序に依存しないことを確認する
np.random.shuffle(seq_colorball_index)
print("shuffled colorball="+str(seq_colorball_index))
print("P(shuffled colorball)="+str(hoppes_urn.P(seq_colorball_index, a=a)))
