def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            answer.append(arr[i]+arr[j])

    answer=list(set(answer))
    answer.sort()
    return answer