# Python3 코딩 테스트 준비



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
