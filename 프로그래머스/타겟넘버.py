# 분류 : 백트래킹 문제
# 문제해결 아이디어 :
# index가 len(numbers)가 될 때까지 number의 '0번 ~ len(numbers)-1번 index'까지 -number 또는 +number 하며 재귀한다.
# 만약 index가 len(numbers)가 되었다면 '0번 ~ len(numbers)-1번 index'까지 모두 계산한 값이므로 그 값 v가 target과 같으면 count한다.
# 재귀기법을 사용하기 때문에 answer을 전역변수로 설정하여 answer에 count한다.

def solution(numbers, target):
    global answer
    answer = 0
    # idx : 인덱스, v : 계산 값

    def find(idx, v):
        global answer
        if idx == len(numbers):
            if v == target:
                answer += 1
            return
        else:
            find(idx+1, v+numbers[idx])
            find(idx+1, v-numbers[idx])

    find(0, 0)
    return answer
