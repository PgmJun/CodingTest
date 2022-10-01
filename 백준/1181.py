import sys
input = sys.stdin.readline

n = int(input().rstrip())   # n입력받기
word_list = list(set(input().rstrip()
                 for _ in range(n)))   # set으로 입력받아 중복단어 제거 후 list로 저장
word_list.sort(key=len)  # 길이 순서로 정렬
max_cnt = len(word_list[-1])    # 제일 긴 단어 길이 저장

result = []
for i in range(1, max_cnt+1):   # 1~max단어길이(i) for문
    for j in word_list:
        if(len(j) == i):    # 리스트에서 단어 길이가 i인 데이터 찾아서 result에 저장
            result.append(j)
    for w in sorted(result):    # 단어길이가 i인 데이터가 저장된 result를 sorted로 정렬 후 출력
        print(w)
    result.clear()  # 길이가 i+1인 데이터를 저장하여 정렬하기 위해 길이가 i인 데이터 삭제
