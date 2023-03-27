from bisect import bisect_left, bisect_right

def solution(score):
    answer = []
    rank = []
    avgScore = []
    
    for s in score:
        avgScore.append(sum(s))
    
    sortAvgScore = sorted(avgScore)
    sortAvgScore.reverse()
    
    for avg in avgScore:
        answer.append(sortAvgScore.index(avg)+1)

    return answer