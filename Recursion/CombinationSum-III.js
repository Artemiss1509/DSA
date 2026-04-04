var combinationSum3 = function(k, n) {
    const arr = []
    
    backtrack(arr,[],n,k,1)
    return arr

    function backtrack(result,arry,target,k,index){
        if(target === 0 && arry.length === k ){
            result.push([...arry])
            return
        }else if(target< 0){
            return
        }
        for(let i =index ;i<10; i++){
            arry.push(i)
            backtrack(result,arry,target-i,k, i+1)
            arry.pop()
        }
    }

};