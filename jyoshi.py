# 若い助詞
import sys

class Jyoshi(object):
	def __init__(self, name, state):
		self.name = name
		self.state = state

	def comingOut(self):
		self.state = "ネカマ"

def kaizuka_bokki(jyoshi):
	if jyoshi.state == "処女":
		return 100
	elif jyoshi.state == "非処女":
		return 80
	else:
		sys.exit("警告： 正体表したね")


jyoshi = Jyoshi("野獣先輩", "処女")
print(jyoshi.name + "は" + str(kaizuka_bokki(jyoshi)) + "点")
jyoshi.comingOut()
print(jyoshi.name + "は" + str(kaizuka_bokki(jyoshi)) + "点")