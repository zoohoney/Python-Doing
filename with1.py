# 1부터 n까지 연속한 숫자의 합 
def sum_n (n) :
    s = 0 
    for i in range(1, n+1) :
        s = s+i
    return s

#print(sum_n(10))
print(sum_n(100))

def sum_ga(n) : 
    return n * (n + 1) // 2

print(sum_ga(10))
