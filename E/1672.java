class Solution {
    
    public int maximumWealth(int[][] accounts) {
        
        int max_wealth = 0;
        
        for ( int[] customer : accounts ) {
            
            int wealth = 0;
            
            for ( int balance :  customer ) {
                
                wealth += balance;
                
            }
            
            if (wealth > max_wealth) max_wealth = wealth;
            
        }
        
        return max_wealth;
        
    }
    
}
