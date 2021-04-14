# 순차 알고리즘
def search_list(a, x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i
    return -1
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 900))

# 7-1 연습문제
def search_list(a, x):
    n = len(a)  
    binlist = []  
    for i in range(0, n):    
        if x == a[i]:         
            binlist.append(i)  

    return binlist  
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 33))

# 7-3 연습문제 
# def find_name():
#     n = ()
#     for i in rnage(0, n):





# number = [39, 14, 67, 105]
# name = ["Justin", "John", "Mike", "Summer"]

# 쉽게 셜명한 선택 정렬 알고리즘
def find_min_idx(a) :
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a) : 
    result = []
    while a :
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result
g = [2, 4, 5, 1, 3]
print(sel_sort(g))

# 일반적인 선택 정렬 알고리즘 
# def sel_sortt(a) :
#     n = len(a)
#     for i in range(0, n -1 ):
#         min_idx = i
#         for j in range(i + 1,  n):
#             if a(j) < a[min_idx]:
#                 min_idx = j
#                 a[i], a[min_idx] = a[min_idx], a[i]
# d = [2, 4, 5, 1, 3]
# sel_sortt(d)
# print(d)

# 쉽게 설명한 삽입 정렬 알고리즘
def find_ins_idx(r,v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result
d = [2, 4, 5, 1, 3]
print(ins_sort(d))

# 일반적인 삽입 정렬 알고리즘 
def ins_sortt(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >=0 and a[j] > key:
            a[j + 1] = a[j]
        j -= 1 
    a[j + 1] = key
d = [2, 4, 5, 1, 3]
ins_sortt(d)
print(d)

# 9-1 연습문제
def ins_sort(a):
   n = len(a)
   for i in range(1, n):
       key = a[i]
       j = i - 1
       while j >= 0 and a[j] > key:  # 부등호 방향 뒤집기
           a[j + 1] = a[j]
           j -= 1
       a[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

# 9-2 연습문제 
def ins_sort(a):
   n = len(a)
   for i in range(1, n):
       key = a[i]
       j = i - 1
       while j >= 0 and a[j] < key:  # 부등호 방향 뒤집기
           a[j + 1] = a[j]
           j -= 1
       a[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)