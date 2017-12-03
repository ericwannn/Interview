class BubbleSort {
public:
    int* bubbleSort(int* A, int n) {
        // write code here
        int temp;
        for(int i=n-2; i>=1; i--){
            for(int j=0; j<=i; j++){
                if(A[j]>A[j+1]){
                    temp = A[j];
                    A[j] = A[j+1];
                    A[j+1] = temp;
                }
            }
        }
        return A;
    }
};