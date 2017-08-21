# 俺で遺伝的アルゴリズムしたらダメだで
from syamu_GAme import *
import matplotlib.pyplot as plt
import warnings;warnings.filterwarnings('ignore')
import numpy as np
import random as rnd


junpeiNUM = 100
genomLen = 8
koiniHatten = 0.0	# 交叉率0
atamaOkashi = 0.01
rnd.seed(1919)
junpeis = [Junpei([rnd.randint(0, 1) for i in range(genomLen)]) for j in range(junpeiNUM)]
plt.ion()

best = junpeis[0]
while(best.tensuu != 1):
	best = junpeis[0]
	for j in junpeis:
		j.bokki(lambda g: sum([g[i]*(2**i) for i in range(genomLen)])/(2**genomLen-1))
		j.review(lambda p: p)
		if j.tensuu > best.tensuu:
			best = j

	ps = [j.phenotype for j in junpeis]
	ts = np.array([j.tensuu for j in junpeis]) - 1
	plt.plot([0, 1], [-1, 0])
	plt.plot(ps, ts, ".")
	plt.xlabel("x")
	plt.ylabel("point")
	plt.xlim(0, 1)
	plt.title("warning: " +str(best.tensuu-1)+ "point...")
	plt.pause(0.3)
	plt.clf()

	newJunpeis = []
	for i in range(junpeiNUM//2):
		nj1 = rouletteWheelSelection(junpeis)
		nj2 = rouletteWheelSelection(junpeis)
		nj1.atamaOkashiNarude(lambda g: list(map(lambda i: 1-i if rnd.random()<atamaOkashi else i, g)))
		nj2.atamaOkashiNarude(lambda g: list(map(lambda i: 1-i if rnd.random()<atamaOkashi else i, g)))

		if rnd.random() < koiniHatten:
			zeroPointCrossover(nj1, nj2)

		newJunpeis.append(nj1)
		newJunpeis.append(nj2)

	junpeis = newJunpeis

print("警告: 0点...")
plt.close()
