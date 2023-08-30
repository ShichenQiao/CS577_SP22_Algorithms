import numpy as np

if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		n = int(input())
		data = []
		for i in range(n):
			line = input().split()
			for j in range(len(line)):
				line[j] = np.int32(int(line[j]))
				#line[j] = int(line[j])
			data.append(line)
		data = sorted(data, key=lambda x : x[1])	# sort by finish time
		m = [0]
		for j in range(1, n + 1):
			vj = data[j - 1][2]
			sj = data[j - 1][0]
			
			#max_i = -1
			#for i in range(j):
			#	if data[i][1] <= sj:
			#		max_i = i + 1
			
			i = 0
			low = 0
			high = j - 1
			while low <= high:
				mid = (high + low) // 2
				if data[mid][1] <= sj:
					low = mid + 1
					i = mid + 1
				else:
					high = mid - 1
				
			m.append(max(np.int32(m[j - 1]), np.int32(m[i] + vj)))
		print(m[n])
		