var subsets = function(nums) {
    const result = [];
    
    function genSubset(index, current) {
        result.push([...current]); 
        
        for (let i = index; i < nums.length; i++) {
            current.push(nums[i]);         
            genSubset(i + 1, current);
            current.pop();
        }
    }
    
    genSubset(0, []);
    return result;
};