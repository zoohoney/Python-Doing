# 1부터 n까지 연속한 숫자의 합 
def sum_n (n) :
    s = 0 
    for i in range(1, n+1) :
        s = s+i
    return s
print(sum_n(10))
print(sum_n(100))
#
def sum_ga(n) : 
    return n * (n + 1) // 2
print(sum_ga(10))

# 1부터 n까지 숫자 제곱합을 구하는 for문 
def sum_ge(n) :
    p = 0 
    for z in range(1, n+1) :
        p = p + z * z
    return p 
print(sum_ge(10))

# 최대값 구하는 알고리즘  
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n) :
        if a[i] > max_v:
            max_v = a[i]
    return max_v
v = [17,92,18,33,58,7,33,42]
print(find_max(v))

# 최대값 위치 알려주는 알고리즘 
v = [17,92,18,33,58,7,33,42]
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx
print(find_max_idx(v))

# 최소값 구하는 알고리즘 
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n) :
        if a[i] < max_v:
            max_v = a[i]
    return max_v
v = [17,92,18,33,58,7,33,42]
print(find_max(v))

# 중복된 이름 찾기 
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i+1,n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom","Jerry","Mike","Tom"]
print(find_same_name(name))
name2 = ["Tom","Jerry","Mike","Tom","Mike"]
print(find_same_name(name2))

# 짝을 지을 수 있는 모든 조합 알고리즘 
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                print(a[i],a[j])

name = ["Tom","Jerry","Mike"]
print(find_same_name(name))