class Solution {
    
    public int[] sortArrayByParity(int[] A) {
        
        int swapped = 0;
        
        for ( int i = 0; i < A.length - swapped ; ) {
            
            if ( A[i] % 2 == 0 ) {

                i++;
                
            } else {
                
                int temp = A[i];
                
                A[i] = A[A.length - 1 - swapped];
                
                A[A.length - 1 - swapped] = temp;
                    
                swapped++;
                
            }
            
        }
        
        return A;
        
    }
    
}
