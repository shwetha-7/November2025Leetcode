class IncrementSubmatricesbyOne{
    private class Solution{
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] mat = new int[n][n];
        for(int query[]:queries){
            int row1=query[0],row2=query[2];
            for(int i=row1;i<row2+1;i++){
                mat[i][query[1]]+=1;
                if(query[3]+1<n){
                    mat[i][query[3]+1]-=1;
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=1;j<n;j++){
                mat[i][j]+=mat[i][j-1];
            }
        }
     

        return mat;
    }
    }
}