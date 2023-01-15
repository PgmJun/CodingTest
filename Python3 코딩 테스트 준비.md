# Python3 코딩 테스트 준비

## 튜플, 리스트, 딕셔너리, 세트

### 선언

**리스트/list** : 대괄호 [ ]
```
# 일반적인 배열

# 선언
l = [1,2,3]
```

**튜플/tuple** : 소괄호 ( )
```
# 값을 변경하지 못하는 배열

# 선언
t1 = (1,2,3)
```

**세트/set** : 중괄호 { }
```
# 인덱스(순서), 중복이 없는 데이터 집합

# 선언
s = {1,2,3}
```

**딕셔너리/dictionary** : 중괄호 { }
```
# Key, Value 로 이루어진 데이터 집합

# 선언
d = {'a':1, 'b':2 ... 'z':27}
```

## 주로 사용되는 문법

**📝 숫자 여러 개 받아 배열에 저장시키기**

```
a = list(map(int,input().split()))
print(a)
```

![image-20220515220920066](https://user-images.githubusercontent.com/84304802/168474632-bdffe36d-99cf-4c90-ad3d-cf6c41c63ae0.png)

---

**📝 숫자 여러 개 받아 각각 변수에 저장시키기**

```
a,b,c = map(int,input().split())
print(a,b,c)
```

![image](https://user-images.githubusercontent.com/84304802/168474594-492fe0e7-ea97-4ee4-9dd6-5aeb0e7c2728.png)

---

**📝 for문으로 list 채우기**

```
a = [2*i for i in range(1,10)]
print(a)
```
list를 받을 때 반복문을 사용해서 list를 채울 때 보통 아래와 같이 입력하지만 위처럼 배열[]안에 위와 같이 [함수 for문] 형태로 작성해주면 간단하게 입력받을 수 있다.

```
a = []
for i in range(1,10):
	a.append(i*2)
print(a)
```
---

**📝 문자 여러 개 받기 모음**

```
#1. 값 두 개를 입력받아 변수 a와 b에 저장 (띄어쓰기 구분)
a, b = input().split() #문자열로
a, b = map(int, input().split()) #정수형으로
a, b = map(float, input().split()) #실수형으로 

#2. 1차원 배열 입력받기 = 정수형 리스트로 저장
num_list = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 

#3. 문자열 여러줄 입력받기 
s_list = [input() for _ in range(n)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)

#4. 한 문자열(숫자ex.12345) 받아서 한 글자씩 나누어 더하기
s = input()
for i in range(len(s)):
	sum += int(s[i])  #문자열은 슬라이싱 가능!! + 문자열 형변환

#5. 띄어쓰기 없이 정수 여러개 입력받아 2차원 배열로 저장하기 
two_d = [list(map(int, input())) for _ in range(n)] #예시는 4줄 입력받음

#6. 열은 띄어쓰기로 행은 엔터로 구분하여 입력받아 2차원 배열 저장하기
t_d = [list(map(int, input().split())) for _ in range(n)]#예시는 4줄. 4.-와 결과는 같다
```

---

**📝 입력 시간 줄이기**

**1. input() 입력시간 줄이기**
```
import sys
input=sys.stdin.readline
```
![image](https://user-images.githubusercontent.com/84304802/168474680-318ddc6d-15b9-4d4f-83d4-41e3e29138fc.png)

<br>

**2. List 사용했는데 시간초과 나오면 set으로 변경 가능한 부분은 변경하기**
**순서가 중요하지 않은 list**
<br>
또는 **배열안에 값이 있는지 확인하기 위해서만 사용할 목적**이라면 set()을 사용하여 값을 저장한다.
```
a = list(map(int,input().split()))
->
a = set(map(int,input().split()))
```

---

**📝 조건부 표현식(if else문 한 줄에 작성)**

```
score = 85
result = "Success" if score > 80 else "Fail"
```

![image](https://user-images.githubusercontent.com/84304802/168476074-bd7f0c22-0af5-4a77-a068-74fcdfb34927.png)

---

**📝 global 전역 변수**

```
a = 0
def plus():
  global a
  a+=1
```

![image](https://user-images.githubusercontent.com/84304802/168476732-d0483aa6-7695-445e-a7fc-822c624b59ea.png)

---

**📝 람다 표현식 - 함수를 간단하게**

```
print((lambda a,b:a + b)(3,7))
```

![image](https://user-images.githubusercontent.com/84304802/168477179-7d209ce5-f30a-451c-a6f3-76f13e7d815a.png)

<br>

```
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b:a+b, list1,list2)
print(list(result))
```

![image](https://user-images.githubusercontent.com/84304802/168477567-12be3dbc-6262-4357-b3f4-b0c6264f00f4.png)

---

**📝 방향 벡터**

![image](https://user-images.githubusercontent.com/84304802/169856951-6ae880b3-579e-41fa-9543-088065df049e.png)

---

**📝 스택(stack) 구현**
<br>
스택: LIFO구조(Last In First Out)<br>
프링글스통 모양의 구조 / 마지막에 들어온 값이 먼저 나감<br>

```
stack = list() #스택 선언

stack.append(1) #스택에 값 추가
stack.pop() #마지막에 들어온 값 제거

print(stack) #스택 출력
print(stack[::-1]) #스택 역순으로 출력
```


---

**📝 큐(queue) 구현**
<br>
: FIFO구조(First In First Out)<br>
배기관 모양의 구조 / 처음에 들어온 값이 먼저 나감<br>

```
from collections import deque

queue = deque() #큐 선언

queue.append(1) #큐에 값 추가
queue.popleft() #큐에 값 제거
```

![image](https://user-images.githubusercontent.com/84304802/173166589-24ead85b-8853-4586-9e91-1daa88537cd7.png)


---

**📝 DFS 탐색**
<br>
스택 구조 사용<br>
재귀적 성질 가짐<br>

```
def dfs(graph, v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph,1,visited)

```

---

**📝 BFS 탐색**
<br>
큐 구조 사용<br>

```
from collections import deque

#BFS 메서드 정의
def bfs(graph,start,visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현
visited = [False] * 9

#BFS 함수 호출
bfs(graph,1,visited)


```

---

**📝 삼항 연산자**
<br>
```
[true_value] if [condition] else [false_value]
```

---

**📝 바다 코끼리 연산자 :=**
<br>
```
# 조건문 내부에서 s에 input()값을 대입하여 즉석에서 while문의 조건 판단
while(s:= input()) != 0:
    print(s)
```

---

**📝 집합(&, |)**

### 합집합
```
a = {1, 2, 3}
b = {1, 2}

a |= b
print(a)
```

![image](https://user-images.githubusercontent.com/84304802/195637199-3dc9ea37-5831-44d6-91eb-06d68864c16e.JPG)
### 교집합
```
a = {1, 2, 3}
b = {1, 2}

a &= b
print(a)
```

![image](https://user-images.githubusercontent.com/84304802/195637210-e5ec5b39-22de-4632-b5df-fd908eee441b.JPG)

---
