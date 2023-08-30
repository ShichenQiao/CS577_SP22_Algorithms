if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		temp = input().split()
		n = int(temp[0])
		m = int(temp[1])
		f = 0
		G = []
		for i in range(m):
			temp = input().split()
			s = int(temp[0])
			d = int(temp[1])
			c = int(temp[2])
			G.append([s, d, c])
		
		while True:
			# DFS
			p = []
			visited = []
			for i in range(len(G) + 1):
				p.append(None)
				visited.append(False)
			stack = [1]
			while len(stack) > 0:
				breaker = False
				u = stack.pop()
				if not visited[u]:
					visited[u] = True
					for i in range(1, len(G)):
						d = G[i][1]
						if G[i][0] == u and not visited[d]:
							p[d] = [u, i]
							if d == n:
								breaker = True
								break
							stack.append(d)
				if breaker:
					break
			
			# find path
			path = [n]
			edge_idx = []
			t = path[len(path) - 1]
			while t > 0:
				t = path[len(path) - 1]
				if t < len(p) and p[t] == None:
					if t != 1:
						path = None
					break
				path.append(p[t][0])
				edge_idx.append(p[t][1])
			
			if path == None:
				break
			
			bn = 2147483647
			for i in range(len(edge_idx)):
				if G[edge_idx[i]][2] > 0 and G[edge_idx[i]][2] < bn:
					bn = G[edge_idx[i]][2]
			
			if bn < 0:
				bn = 0
			
			for i in range(len(edge_idx)):
				G[edge_idx[i]][2] = G[edge_idx[i]][2] - bn
				found = False
				for j in range(len(G)):
					if G[j][1] == G[edge_idx[i]][0] and G[j][0] == G[edge_idx[i]][1]:
						G[j][2] = G[j][2] + bn
						found = True
						break
				if not found:
					G.append([G[edge_idx[i]][1], G[edge_idx[i]][0], bn])
			
			f = f + bn

		print(f)