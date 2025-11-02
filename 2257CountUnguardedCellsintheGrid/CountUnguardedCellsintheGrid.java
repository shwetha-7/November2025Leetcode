public class CountUnguardedCellsintheGrid {
    private class Solution{
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
          int count=0;     
          int[][] grid=new int[m][n];
          for(int[] guard:guards){
            grid[guard[0]][guard[1]]=3;
          }  
          for(int[] wall:walls){
            grid[wall[0]][wall[1]]=1;
          }  

          for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==3){
                    checkLeft(i,j, grid);
                    checkRight(n, i,j, grid);
                    checkTop(i, j, grid);
                    checkBottom(m, i, j, grid);
                }
            }
          }
          for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0){
                    count++;
                }
            }
          }

          return count;
      }
    // check left
    public void checkLeft(int row,int col,int[][] grid){
        for(int j=col-1; j>0 ;j--){
            if(grid[row][j]==3 || grid[row][j]==1){
                return;
            }
            grid[row][j]=2;
        }

    }
    // check right 
        public void checkRight(int n,int row,int col,int[][] grid){
        for(int j=col+1; j<n ;j++){
            if(grid[row][j]==3 || grid[row][j]==1){
                return;
            }
            grid[row][j]=2;
        }
    }
    // check top 
    // 
    public void checkTop(int row,int col,int[][] grid){
        for(int i=row-1; i>0 ;i--){
            if(grid[i][col]==3 || grid[i][col]==1){
                return;
            }
            grid[i][col]=2;
        }
    }
    // check Bottom
    public void checkBottom(int n,int row,int col,int[][] grid){
        for(int i=row+1; i<n ;i++){
            if(grid[i][col]==3 || grid[i][col]==1){
                return;
            }
            grid[i][col]=2;
        }
    }
    }
}
