class Solution {
    
public:
    
    string generateTheString(int n) {
        
        string ans = "";
        
        if( n % 2 == 0 ) {
            
            ans = "x";
            
            n--;
            
        }
        
        for (int i = 0; i < n; i++) {
            
            ans += "a";
            
        }
        
        return ans;
        
    }
    
};
