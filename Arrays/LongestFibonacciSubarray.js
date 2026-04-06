var longestSubarray = function(nums) {
    if(nums.length === 1 || nums.length===2){
        return nums.length
    }
    let out = 0
    let count = 1
    let right = 2
    for(let i=0;i<nums.length;i++){
        if(nums[i]+nums[i+1]=== nums[i+2]){
            count+=1
        }else{
            count=1
        }
        out = count > out ? count : out;
    }
    return out+1
};