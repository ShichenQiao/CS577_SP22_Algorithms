def CountSort(A):
	l = len(A)
	if l == 1:
		return (A, 0)
	else:
		(A1, c1) = CountSort(A[0 : int(l/2)])
		(A2, c2) = CountSort(A[int(l/2) :])
		(A, c) = MergeCount(A1, A2)
		return (A, c + c1 + c2)

def MergeCount(A, B):
	S = []
	c = 0
	while len(A) > 0 and len(B) > 0:
		if A[0] <= B[0]:
			S.append(A[0])
			A.pop(0)
		else:
			S.append(B[0])
			B.pop(0)
			c += len(A)
	if len(B) == 0:
		return (S + A, c)
	else:
		return (S + B, c)


if __name__ == "__main__":
	I = int(input())
	while I > 0:
		I -= 1
		n = int(input())
		A = input().split(' ')
		for i in range(n):
			A[i] = int(A[i])
		_, c = CountSort(A)
		print(c)
		