import java.util.ArrayList;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        
        if (target.length == 0) { return new ArrayList<String>(); } 
        
        List<String> operations = new ArrayList<String>();
        
        int prev = 0;
        for ( int i : target ) {
            if ( i != prev + 1 ) {
                for ( int j = 1; j < i - prev; j++ ) {
                    operations.add("Push");
                    operations.add("Pop");
                }
            }
            operations.add("Push");
            prev = i;
        }
        
        return operations;
    }
}
