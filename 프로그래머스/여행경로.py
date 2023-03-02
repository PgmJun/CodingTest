from collections import deque
from copy import deepcopy


def solution(tickets):
    answer = []
    usedTicketsArr = []
    queue = deque([("ICN",list(),deepcopy(tickets))])
    
    while queue:
        airport, visitedTickets, unusedTickets = queue.popleft()
        if len(unusedTickets) == 0:
            usedTicketsArr.append(visitedTickets)
            continue
        for t in unusedTickets:
            if t[0] == airport:
                uuts = deepcopy(unusedTickets)
                vts = deepcopy(visitedTickets)
                uuts.remove(t)
                vts.append(t)
                queue.append([t[1],vts,uuts])
            
    
    usedTicketsArr.sort()
    answer.append("ICN")
    for ut in usedTicketsArr[0]:
        answer.append(ut[1])
    
    return answer