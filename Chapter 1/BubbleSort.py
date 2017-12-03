class BubbleSort:
    def bubbleSort(self, A, n):
        for i in range(n-1, 0, -1):
            for j in range(i):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A