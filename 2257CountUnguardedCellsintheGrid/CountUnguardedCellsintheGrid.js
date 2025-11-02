/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    let grid=[]
    for(let i=0;i<m;i++){
        grid.push([])
        for(let j=0;j<n;j++){
            grid[i].push(0)
        }
    }


    
    // check left
    var checkLeft=(row,col,grid)=>{
        for(let j=col-1;j>=0;j--){
            if(grid[row][j]==3 || grid[row][j]==1){
                return 
            }
            grid[row][j]=2
        }
    }
    // check right
    var checkRight=(n,row,col,grid)=>{
        for(let j=col+1;j<n;j++){
            if(grid[row][j]==3 || grid[row][j]==1){
                return 
            }
            grid[row][j]=2
        }
    }
    // check top
    var checkTop=(row,col,grid)=>{
        for(let i=row-1;i>=0;i--){
            if(grid[i][col]==3 || grid[i][col]==1){
                return 
            }
            grid[i][col]=2
        }
    }
    // check Bottom 
    var checkBottom=(m,row,col,grid)=>{
        for(let i=row+1;i<m;i++){
            if(grid[i][col]==3 || grid[i][col]==1){
                return 
            }
            grid[i][col]=2
        }
    }

    for(let guard in guards){
        grid[guard[0]][guard[1]]=3
    }
    for(let wall in walls){
        grid[wall[0]][wall[1]]=1
    }

    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(grid[i][j]==3){
                checkLeft(i,j,grid)
                checkRight(n,i,j,grid)
                checkTop(i,j,grid)
                checkBottom(m,i,j,grid)
            }
        }
    }

    let count=0;
    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(grid[i][j]==0){
               count++;
            }
        }
    }

    return count



};