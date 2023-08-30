if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		temp = input().split()
		n = int(temp[0])
		W = int(temp[1])
		M = [[0 for x in range(W + 1)] for y in range(n + 1)]
		v = [0]
		w = [0]
		for i in range(n):
			temp = input().split()
			w.append(int(temp[0]))
			v.append(int(temp[1]))
		for i in range(1, n + 1):
			for j in range(1, W + 1):
				x = 0
				if w[i] <= j:
					M[i][j] = max(M[i - 1][j], M[i - 1][j - w[i]] + v[i])
				else:
					M[i][j] = M[i - 1][j]
		print(M[n][W])
		
		print(M)