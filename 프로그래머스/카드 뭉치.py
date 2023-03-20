def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx1 = 0
    idx2 = 0

    while True:
        if len(goal) == 0:
            break

        word = goal[0]
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
            goal.remove(word)

        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
            goal.remove(word)

        else:
            answer = 'No'
            break

    return answer
