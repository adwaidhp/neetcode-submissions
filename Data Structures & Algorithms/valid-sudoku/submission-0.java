class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> seen= new HashSet<>();
        for (int r=0;r<9;r++){
            for (int c=0;c<9;c++){
                char ch= board[r][c];
                if (board[r][c]=='.') continue;
                String row = ch + " in row " + r;
                String col = ch + " in col " + c;
                String square = ch + " in square " + (r/3) + '-' + (c/3);

                if (!seen.add(row)||!seen.add(col)||!seen.add(square)){
                    return false;
                }
            }
        }
        return true;
    }
}
