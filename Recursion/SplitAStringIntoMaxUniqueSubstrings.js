var maxUniqueSplit = function(s) {
    const arr = []
    const d = new Set()
    max = 0
    backtrack(arr,'',s,0,d,0)
    return max

    function backtrack(result,current,s,index,d,count){
        if(index===s.length){
            max= Math.max(max, count)
            return
        }
        for(let i = index; i<s.length;i++){
            current =s.slice(index, i + 1)
            if(!d.has(current)){
                d.add(current)
                backtrack(result,current,s,i+1,d,count+1)
                d.delete(current)
            }
            
        }
    }
};