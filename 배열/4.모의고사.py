def solution(arr):
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    list = [0,0,0]

    for i in range(len(pattern)):
        count = 0
        for j in range(len(arr)):
            if(pattern[i][j%len(pattern[i])]==arr[j]):
                count +=1
        list[i] = count
    
    max_score = max(list)
    higest_scores = []

    for i,score in enumerate(list):
        if score == max_score:
            higest_scores.append(i+1)

    return higest_scores