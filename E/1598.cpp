class Solution {
    
public:
    
    int minOperations(vector<string>& logs) {
        
        int deg = 0;
        
        for ( auto op : logs ) {
            
            if ( op == "../") {
                
                if (deg > 0 ) --deg;
                
            } else if (op == "./") {
                
                // pass
                
            } else {
                
                ++deg;
                
            }
            
        }
        
        return deg;
        
    }
    
};
