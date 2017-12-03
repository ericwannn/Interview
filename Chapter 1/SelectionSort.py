class SelectionSort:
    def selectionSort(self, A, n):
        # write code here
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if A[j] < A[index]:
                    index = j
            A[i], A[index] = A[index], A[i]
        return A