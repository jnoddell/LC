import java.lang.*;

class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        
        char selected = board[click[0]][click[1]];
        
        if (selected == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        
        // Empty space found, return number of bombs if any
        
        int cols = board[0].length;
        int rows = board.length;
        int bombsNearby = 0;
        
        // check for nearby bombs
        for (int r = Math.max(0, click[0]-1); r <= Math.min(rows-1, click[0]+1); r++) {
            for (int c = Math.max(0, click[1]-1); c <= Math.min(cols-1, click[1]+1); c++) {
                if (board[r][c] == 'M') bombsNearby += 1;
        }   
        }
        
        if (bombsNearby > 0)  {
            bombsNearby += 48;
            board[click[0]][click[1]] = (char) bombsNearby;
            return board;
        } else {
            board[click[0]][click[1]] = 'B';
            for (int r = Math.max(0, click[0]-1); r <= Math.min(rows-1, click[0]+1); r++) {
                for (int c = Math.max(0, click[1]-1); c <= Math.min(cols-1, click[1]+1); c++) {
                    if (board[r][c] == 'M' || board[r][c] == 'E') {
                        int[] nextClick = {r, c};
                        board = updateBoard(board, nextClick);
                    }
                }   
             }
        }
        
        return board;
        
    }
}
