# # 일반적인 병합 정렬 알고리즘 
# def merge_sort(a):
#     n = len(a)
#     # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
#     if n <= 1:
#         return
#     # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
#     mid = n // 2
#     g1 = a[:mid]
#     g2 = a[mid:]
#     merge_sort(g1)
#     merge_sort(g2)
#     # 두 그룹을 합치는 과정(병합)
#     i1 = 0
#     i2 = 0
#     ia = 0
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] < g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
#     #아직 남아 있는 자료들을 결과에 추가
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort(d)
# print(d)

# # 문제 10-1 내림차순 병합 정렬
# def merge_sort(a):
#     n = len(a)
#     if n <= 1:
#         return
#     mid = n // 2
#     g1 = a[:mid]
#     g2 = a[mid:]
#     merge_sort(g1)
#     merge_sort(g2)
#     i1 = 0
#     i2 = 0
#     ia = 0
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] > g2[i2]:  # 부등호 방향 뒤집기
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort(d)
# print(d)

# 퀵정렬 알고리즘 
def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    #재귀 호출 부분 
    quick_sort_sub(a, start, i -1)
    quick_sort_sub(a, i+1,end)
def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)

# 문제 11-1 거품 정렬
def bubble_sort(a):
    n = len(a)
    while True:  # 정렬이 완료될 때까지 계속 수행
        changed = False  # 자료를 앞뒤로 바꾸었는지 여부
        # 자료를 훑어 보면서 뒤집힌 자료가 있으면 바꾸고 바뀌었다고 표시
        for i in range(0, n - 1):
            if a[i] > a[i + 1]: # 앞이 뒤보다 크면
                print(a)        # 정렬 과정 출력(참고용)
                a[i], a[i + 1] = a[i + 1], a[i]  # 두 자료의 위치를 맞바꿈
                changed = True  # 자료가 앞뒤로 바뀌었음을 기록
        # 자료를 한 번 훑어보는 동안 바뀐 적이 없다면 정렬이 완성된 것이므로 종료
        # 바뀐 적이 있으면 다시 앞에서부터 비교 반복
        if changed == False:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
