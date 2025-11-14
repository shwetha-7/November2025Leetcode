/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function(n, queries) {
    let mat=[];
    for(let i=0;i<n;i++){
        let temp=[]
        for(let j=0;j<n;j++){
            temp.push(0)
        }
        mat.push(temp.slice());
    }

    for(let k=0;k<queries.length;k++){
        let query=queries[k];
        let row1=query[0],row2=query[2];
        for(let i=row1;i<row2+1;i++){
            mat[i][query[1]]+=1;
            if(query[3]+1<n){
                mat[i][query[3]+1]-=1
            }
        }

    }

    for(let i=0;i<n;i++){
        for(let j=1;j<n;j++){
            mat[i][j]+=mat[i][j-1]
        }
    }

    return mat
};