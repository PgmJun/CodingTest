n,m = map(int, input().split())
groups = dict()

TEAM = 0
MEMBER = 1

for _ in range(n):
    groupName = input()
    memberCnt = int(input())
    members = list()

    for _ in range(memberCnt):
        members.append(input())
    groups[groupName] = sorted(members)

for _ in range(m):
    quiz = input()
    type = int(input())

    if(type == TEAM):
        for g in groups:
            if quiz == g:
                for member in groups[g]:
                    print(member)
                break
            
    elif(type == MEMBER):
        for g in groups:
            if quiz in groups[g]:
                print(g)
                break