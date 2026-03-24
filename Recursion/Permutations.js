var permute = function(nums) {
    const result = []
    const used = new Array(nums.length).fill(false)
    backtrack(result,[],nums,used);
    return result

    function backtrack(result,current,nums,used){
        if(current.length === nums.length){
            result.push([...current])
            return
        }
        for(let i =0; i<nums.length; i++ ){
            if(!used[i]){
                current.push(nums[i])
                used[i] = true
                backtrack(result,current,nums,used)
                used[i] = false
                current.pop()
            }
        }
    }
    
};