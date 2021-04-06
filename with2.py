# 팩토리얼 알고리즘 
## 연속한 숫자의 곱 알고리즘 
def fact(n) :
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f 
print(fact(5))

# 재귀호출을 이용한 팩토리얼 
def jfact(n):
    if n <=1:
        return 1
    return n * jfact(n - 1)
print(jfact(5))

# 문제 1. 1부터 n까지의 합 구하기(재귀 호출)
def sum(n):
    if n <=1:
        return 1
    return n + sum(n - 1)
print(sum(3))

# 문제 2. 숫자 n개 중에서 최댓값 찾기(재귀호출)
# def jfind_max(n):
#     i = len(n)
#     max_v = n[0]
#     if i <= 1:
#         return 1 
#     for i in range(1, n) :
#         if n[i] > max_v:
#             max_v = n[i]
#     return max_v
# v = [17,92,18,33,58,7,33,42]
# print(jfind_max(v))


# def find_max(a):
#     n = len(a)
#     max_v = a[0]
#     for i in range(1, n) :
#         if a[i] > max_v:
#             max_v = a[i]
#     return max_v
# v = [17,92,18,33,58,7,33,42]
# print(find_max(v))