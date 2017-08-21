# 交叉率0
import random as rnd

# 大物agent最適解誰も行けずへこむ
class Junpei(object):
    def __init__(self, genotype):
        self.tensuu = 0.0
        self.genotype = genotype
        self.phenotype = None

    def bokki(self, func):
        self.phenotype = func(self.genotype)
 
    def review(self, func):
        self.tensuu = func(self.phenotype)

    def atamaOkashiNarude(self, func):  
        self.genotype = func(self.genotype)

# ルーレット選択でございまｽｩｩｩｩｩｩｩ
def rouletteWheelSelection(junpeis):
    r = sum([i.tensuu for i in junpeis]) * rnd.random()
    for i in junpeis:
        r -= i.tensuu
        if r<=0:
            return(i)

# ｺｳｻﾆﾊｯﾃﾝｼﾃ...素敵なことやないですか
def zeroPointCrossover(j1, j2):
    point= rnd.randint(0, 0)
    for i in range(0, 0):
        j1.genotype[i], j2.genotype[i] = j2.genotype[i], j1.genotype[i]
