if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		l = int(input())	# num page
		n = int(input())	# num request
		pages = {}
		cache = []
		requests = input().strip().split(" ")
		for i in range(len(requests)):
			data = int(requests[i])
			requests[i] = data
			if data not in pages:
				pages[data] = [i]
			else:
				pages[data].append(i)
		cnt = 0
		for i in range(len(requests)):
			req = requests[i]
			if req not in cache:
				cnt += 1
				if len(cache) == l:
					furthest = -1
					furthest_set = False
					max = -1
					for d in cache:
						temp = -1
						for idx in pages[d]:
							if idx > i:
								temp = idx
								break
							if idx == pages[d][len(pages[d]) - 1]:
								furthest = d
								furthest_set = True
						if furthest_set:
							break
						if temp > max:
							max = temp
							furthest = d
					if furthest in cache:
						cache.remove(furthest)
				cache.append(req)
		print(cnt)
