# 한수는 지금 (x, y)에 있다.
# 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

x, y, w, h = map(int, input().split())
hansuToRectV = w-x  # 한수와 직사각형 오른쪽 끝의 x차이
hansuToRectH = h-y  # 한수와 직사각형 오른쪽 끝의 y차이


if hansuToRectV > hansuToRectH:  # y차이가 x차이보다 작을 때
    if hansuToRectH > x or hansuToRectH > y:  # 한수가 왼쪽과 더 가깝지 않은 지 비교
        print(x) if x < y else print(y)
    else:
        print(hansuToRectH)
elif hansuToRectV < hansuToRectH:  # x차이가 y차이보다 작을 때
    if hansuToRectV > x or hansuToRectV > y:  # 한수가 왼쪽과 더 가깝지 않은 지 비교
        print(x) if x < y else print(y)
    else:
        print(hansuToRectV)
else:  # x,y차이 값이 같을 때
    # 한수가 왼쪽과 더 가깝지 않은 지 비교(hansuToRectV, hansuToRectH 값이 똑같기 때문에 아무거나)
    if hansuToRectV > x or hansuToRectV > y:
        print(x) if x < y else print(y)
    else:
        print(hansuToRectV)
