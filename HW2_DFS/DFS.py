if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		dict = {}
		visited = {}
		stack = []
		nodes = []
		n = int(input())
		for i in range(n):
			line = input()
			row = line.split(' ')
			nodes.append(row[0])
			if len(row) == 1:
				dict[row[0]] = None
			else:
				dict[row[0]] = row[1:]
			visited[row[0]] = False
		
		stack.append(nodes[0])
		
		while len(stack) > 0:
			u = stack.pop()
			if not visited[u]:
				if len(nodes) == 1:
					print(u)
				else:
					print(u + " ", end='')
				visited[u] = True
				nodes.remove(u)
				if dict[u] != None:
					temp = reversed(dict[u])
					for r in temp:
						stack.append(r)
			if len(nodes) > 0 and len(stack) == 0:
				stack.append(nodes[0])
