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
def jfind_max(a, n):
    if n == 1:
        return a[0]
    max_n = jfind_max(a, n -1)
    if max_n > a[n - 1] :
        return max_n
    else:
        return a[n - 1]
v = [17,92,18,33,58,7,33,42]
print(jfind_max(v, len(v)))

# 최대공약수 알고리즘
def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i == 0 :
            return i
        i = i -1 
print(gcd(1,5))

# 유클리드 방식 최대공약수 알고리즘
def ugcd(a,b):
    if b == 0:
        return a
    return ugcd(b, a %b)
print(ugcd(1,5))

# 문제 1. 피보나치 수 (재귀호출)
def fibonaci(n):
    if n <= 1:
        return n  
    return fibonaci(n - 2) + fibonaci(n - 1)
print(fibonaci(7))
print(fibonaci(10))