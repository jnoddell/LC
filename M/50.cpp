class Solution {
public:
    double myPow( double base, int power ) {
        
        if ( power == 0 ) return ( double ) 1;
        
        double adjustment = base;
        
        if( power < 0 ) adjustment = 1 / base;
        
        if( abs( power ) % 2 == 0 ) return myPow( adjustment * adjustment, abs(power / 2) );
        
        return adjustment * myPow( adjustment * adjustment, abs(power / 2) );      
    }
};
