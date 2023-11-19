def solution(numbers, target):
    global answer
    answer = 0
    # idx : 인덱스, v : 계산 값, s : 수식
    def find(idx, v):
        global answer
        if idx == len(numbers):
            if v == target:
                answer += 1
        else:
            find(idx+1,v+numbers[idx])
            find(idx+1,v-numbers[idx])
    
    find(0,0)
    return answer