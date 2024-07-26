def solution(keymap, targets):
    answer = []
    keyObject={}
    
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in keyObject or keyObject[key[i]]>i:
                keyObject[key[i]]=i+1
        
    
    for target in targets:
        num, t=0, True
        for value in target:
            if value not in keyObject:
                answer.append(-1)
                t=False
                break
            num+=keyObject[value]
        else:
            answer.append(num)
            
    
    
    return answer
