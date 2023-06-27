def solution(arr):
    stk = []
    i = 0
    
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif len(stk) > 0:
            if stk[-1] == arr[i]:
                stk = stk[:-1]
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
        i+=1
    if len(stk) == 0:
        stk.append(-1)
    return stk