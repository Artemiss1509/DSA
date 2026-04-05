var partition = function(s) {
    const result = []
    backtrack(result,[],s,0)
    return result;

    function backtrack(result,current,s,index){
        if(index === s.length){
            result.push([...current])
            return
        }
        for(let i = index; i<s.length; i++){
            if(isPalindrome(s,index,i)){
                current.push(s.slice(index,i+1))
                backtrack(result,current,s,i+1)
                current.pop()
            }
        }
    }

    function isPalindrome(s,index,i){
        while(index<i){
            if(s[index++] !== s[i--]){
                return false
            }
        }
        return true
    }
};