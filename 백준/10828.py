import sys
input=sys.stdin.readline

stack = []

for i in range(int(input())):
    read = input().split()
    if(read[0] == "push"):
        stack.append(read[1])
    elif(read[0] == "pop"):
        if(len(stack) == 0): print(-1)
        else:
            pop = stack.pop()
            print(pop)
    elif(read[0] == "top"):
        if(len(stack) == 0): print(-1)
        else: print(stack[-1])
    elif(read[0] == "size"):
        print(len(stack))
    elif(read[0] == "empty"):
        if(len(stack) == 0): print(1)
        else: print(0)
