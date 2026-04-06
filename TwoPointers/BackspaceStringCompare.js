var backspaceCompare = function(s, t) {
    function backspace(s){
        let newStr = ''
        for(let i=0;i<s.length;i++){
            if(s[i] === '#'){
                newStr= newStr.slice(0,-1)
                continue
            }
            newStr += (s[i])
        }
        return newStr
    }

    const newS = backspace(s)
    const newT = backspace(t)


    if(newS.length !== newT.length){
        return false
    }

    for(let i=0;i<s.length;i++){
        if(newS[i] !== newT[i]){
            return false
        }
    }
    return true
};