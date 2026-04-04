var letterCombinations = function(digits) {
    const dig = {
        2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz',
        }
    let arr = []
    backtrack(arr,'',digits,0)
    return arr

    function backtrack(result,a,digits,index){
        if(index===digits.length){
            result.push(a)
            return
        }
        let b = dig[digits[index]]
        for(i of b){
            backtrack(result,a+i,digits,index+1)
        }
    }
}