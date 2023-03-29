def solution(id_list, report, k):
    answer = []
    receiveMail = dict()
    reportCnt = dict()
    reportMember = dict()
    for id in id_list:
        reportCnt[id] = 0
        reportMember[id] = []
        receiveMail[id] = 0
    
    for reportInfoStr in set(report):
        reportInfo = reportInfoStr.split()
        reportUser, reportedUser = reportInfo[0], reportInfo[1]
        
        reportCnt[reportedUser] += 1
        reportMember[reportedUser].append(reportUser)
    
    for key in reportCnt.keys():
        if reportCnt[key] >= k:
            for member in reportMember[key]:
                receiveMail[member] += 1
    
    for key in receiveMail.keys():
        answer.append(receiveMail[key])
    return answer