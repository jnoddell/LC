public class Solution {
    
    public int NumRookCaptures(char[][] board) {
    
        int rook_row = -1;
        
        int rook_col = -1;
        
        int ans = 0;
        
        for ( int row = 0; row < 8; row++ ) {
            
            for ( int col = 0 ; col < 8;  col++ ) {
                
                if ( board[row][col] == 'R') {
                    
                    rook_row = row;
                    
                    rook_col = col;
                    
                    break;
                    
                }
                
            }
            
            if ( rook_row != -1 ) break;
            
        }
        
        if ( rook_col != 0 ) {
            
            for ( int i = rook_col - 1 ; i >= 0 ; i-- ) {
                
                if ( board[rook_row][i] == 'B' ) break;
                
                if ( board[rook_row][i] == 'p' ) {
                    
                    ans++;
                    
                    break;
                    
                }
                
            }
            
        }
        
        if ( rook_col != 7 ) {
            
            for ( int i = rook_col + 1 ; i <= 7 ; i++ ) {
                
                if ( board[rook_row][i] == 'B' ) break;
                
                if ( board[rook_row][i] == 'p' ) {
                    
                    ans++;
                    
                    break;
                    
                }
                
            }
            
        }
        
        if ( rook_row != 0 ) {
            
            for ( int i = rook_row - 1 ; i >= 0 ; i-- ) {
                
                if ( board[i][rook_col] == 'B' ) break;
                
                if ( board[i][rook_col] == 'p' ) {
                    
                    ans++;
                    
                    break;
                    
                }
                
            }
            
        }
        
        if ( rook_row != 7 ) {
            
            for ( int i = rook_row + 1 ; i <= 7 ; i++ ) {
                
                if ( board[i][rook_col] == 'B' ) break;
                
                if ( board[i][rook_col] == 'p' ) {
                    
                    ans++;
                    
                    break;
                    
                }
                
            }
            
        }
        
        return ans;
        
    }
    
}
