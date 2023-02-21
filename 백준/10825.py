import sys
input = sys.stdin.readline

students = []
for _ in range(int(input())):
    students.append(list(input().split()))


for s in sorted(students, key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0])):
    print(s[0])