/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    
    var ans = []
    
    for ( var i = 1; i <= n; i++ ) {
        
        if ( i % 3 == 0 && i % 5 == 0 ) {
            
            ans[i-1] = "FizzBuzz";
            
        } else if ( i % 3 == 0 ) {
            
            ans[i-1] = "Fizz";
            
        }  else if ( i % 5 == 0 ) {
            
            ans[i-1] = "Buzz";
            
        } else {
            
            ans[i-1] = i + "";
            
        }
        
    }
    
    return ans;
    
};
