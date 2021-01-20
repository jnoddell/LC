class Solution {
    
    public boolean judgeCircle( String moves ) {
    
        int displacement_x = 0;
            
        int displacement_y = 0;
        
        for ( int i = 0 ; i < moves.length(); i++ ) {
            
            switch ( moves.charAt(i) ) {
                    
                case 'U':
                    
                    displacement_y++;
                    
                    break;
                    
                case 'D':
                    
                    displacement_y--;
                    
                    break;
                    
                case 'L':
                    
                    displacement_x--;
                    
                    break;
                    
                case 'R':
                    
                    displacement_x++;
                    
                    break;
                    
            }

            
        }
        
        if ( displacement_y == 0 && displacement_x == 0) return true;
        
        return false;
        
    }
}
