from flow_network import MaximumFlow

if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		temp = input().split()
		m = int(temp[0])
		n = int(temp[1])
		q = int(temp[2])
		mf = MaximumFlow(m + n + 2)
		s = []
		for t in range(q):
			temp = input().split()
			i = int(temp[0])
			j = int(temp[1])
			s.append((i, m + j, 1))
			s.append((0, i, 1))
			s.append((m + j, m + n + 1, 1))
		myset = set(tuple(i) for i in s)
		l = list(myset)
		for item in l:
			mf.add_edge(item[0], item[1], item[2])
		result = mf.run(0, m + n + 1)
		if n == m and n == result:
			print(result, "Y")
		else:
			print(result, "N")