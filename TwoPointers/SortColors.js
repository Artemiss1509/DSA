var sortColors = function(nums) {
    let left = 0
    let right = nums.length - 1
    let mid = 0

    while(mid<=right){
        if(nums[mid] === 0){
            nums[mid] = nums[left]
            nums[left] = 0
            left++
            mid++
        }else if(nums[mid] === 2){
            nums[mid] = nums[right]
            nums[right] = 2
            right--
        }else if( nums[mid] === 1){
            mid++
        }
    }
}   