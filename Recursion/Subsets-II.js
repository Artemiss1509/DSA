var subsets = function(nums) {
    const result = [];
    nums.sort()
    
    function genSubset(index, current) {
        result.push([...current]); 
        
        for (let i = index; i < nums.length; i++) {
            if (i > index && nums[i] === nums[i - 1]) continue;
            current.push(nums[i]);         
            genSubset(i + 1, current);
            current.pop();
        }
    }
    
    genSubset(0, []);
    return result;
};