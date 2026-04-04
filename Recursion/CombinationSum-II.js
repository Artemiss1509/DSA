var combinationSum2 = function(candidates, target) {
    candidates.sort()
    const arr = []
    
    backtrack(arr,[],target,candidates,0)
    return arr

    function backtrack(result,arry,target,candidates,index){
        if(target === 0 ){
            result.push([...arry])
            return
        }else if(target< 0){
            return
        }
        for(let i =index ;i<candidates.length; i++){
            if (i > index && candidates[i] === candidates[i - 1]) continue;
            arry.push(candidates[i])
            backtrack(result,arry,target-candidates[i],candidates, i+1)
            arry.pop()
        }
    }
};