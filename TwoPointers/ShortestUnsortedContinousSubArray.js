var findUnsortedSubarray = function(nums) {
    let n = nums.length;
    let max = -Infinity;
    let min = Infinity;
    let end = -1;
    let start = 0;

    for (let i = 0; i < n; i++) {
        max = Math.max(max, nums[i]);
        if (nums[i] < max) {
            end = i;
        }
    }
    for (let i = n - 1; i >= 0; i--) {
        min = Math.min(min, nums[i]);
        if (nums[i] > min) {
            start = i;
        }
    }
    return end === -1 ? 0 : end - start + 1;
};