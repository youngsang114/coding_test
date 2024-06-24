def solution(N,stages):
   
    counts = [0 for _ in range(N+2)]
    
    for i in stages:
        counts[i] +=1
    
    fails ={}

    for i in range(1,N+1):
        if counts[i] ==0:
            fails[i] = 0
            continue
            
        fails[i] = counts[i] / sum(counts[i:])
    
    result =sorted(fails,key= lambda x : fails[x], reverse=True)

    return result
    


   