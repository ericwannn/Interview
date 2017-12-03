class SelectionSort {
public:
    int* selectionSort(int* A, int n) {
        // write code here
        int index, temp;
        for(int i=0; i<n; i++){
            index = i;
            for(int j=i+1; j<n;j++){
                if(A[j] < A[index]){
                    index = j;
                }
            }
            temp = A[i];
            A[i] = A[index];
            A[index] = temp;
        }
        return A;
    }
};