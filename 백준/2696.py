import heapq

def findMid(numArr):
    heapArr = []
    for n in numArr:
        heapq.heappush(heapArr,n)
    result = []
    for _ in range(int(len(heapArr)/2)+1):
        result.append(heapq.heappop(heapArr))

    return result[-1]

def findMidValues(nums):
    numArr = []
    result = []
    for i in range(len(nums)):
        numArr.append(nums[i])
        if (i+1) % 2 == 1:
            result.append(findMid(numArr))
    
    print(len(result))
    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print()
        print(result[i],end=' ')

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    for i in range(int(m/10)+1):
        nums += (list(map(int,input().split())))

    findMidValues(nums)