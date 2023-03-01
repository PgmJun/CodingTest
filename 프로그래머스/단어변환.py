from collections import deque


def IsDifferenceCntOne(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            print(word1[i], word2[i])
            cnt += 1
        if cnt > 1:
            break
    return cnt


def solution(begin, target, words):
    answer = 0
    queue = deque([(begin, 0)])
    visited = [False] * len(words)

    while queue:
        w, cnt = queue.popleft()
        if w == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visited[i]:
                continue
            if IsDifferenceCntOne(words[i], w) == 1:
                queue.append([words[i], cnt+1])
                visited[i] = True

    return answer
