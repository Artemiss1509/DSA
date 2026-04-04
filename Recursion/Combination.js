var combine = function(n, k) {
    const arr = []
    
    backtrack(arr,[],n,k,1)
    return arr

    function backtrack(result,arry,n,k,index){
        if(arry.length === k ){
            result.push([...arry])
            return
        }
        for(let i =index ;i<n+1; i++){
            arry.push(i)
            backtrack(result,arry,n,k, i+1)
            arry.pop()
        }
    }

};