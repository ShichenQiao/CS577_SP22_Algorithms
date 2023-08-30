import random

if __name__ == "__main__":
	n = int(input())
	m = int(input())
	C = []
	for i in range(m):
		temp = input().split(" ")
		temp[0] = int(temp[0])
		temp[1] = int(temp[1])
		temp[2] = int(temp[2])
		C.append(temp)
	while True:
		assignment = [False]
		for i in range(n):
			assignment.append(bool(random.getrandbits(1)))
		cnt = 0
		for i in range(m):
			a = False
			b = False
			c = False
			cnt = cnt + 1
			if C[i][0] > 0:
				a = assignment[C[i][0]]
			else:
				a = not assignment[-C[i][0]]
			if C[i][1] > 0:
				b = assignment[C[i][1]]
			else:
				b = not assignment[-C[i][1]]
			if C[i][2] > 0:
				c = assignment[C[i][2]]
			else:
				c = not assignment[-C[i][2]]
			if not (a or b or c):
				cnt = cnt - 1
		if cnt > (m * 7 / 8):
			rst = ""
			for i in range (1, n):
				if assignment[i]:
					rst = rst + "1 "
				else:
					rst = rst + "-1 "
			if assignment[n]:
				rst = rst + "1"
			else:
				rst = rst + "-1"
			print(rst)
			break
			