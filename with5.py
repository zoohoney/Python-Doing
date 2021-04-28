# 회문 찾긱 알고리즘 
# def palindrome(s):
#     #큐와 스택을 리스트로 정의 
#     qu = []
#     st = []
#     #1단계: 문자열의 알파벳 문자를 각가 큐와 스택에 넣음 
#     for x in s:
#         #해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
#         #큐와 스택에 각각 그 문자를 추가 
#         if x.isalpha():
#             qu.append(x.lower())
#             st.append(x.lower())
#     # 2단계: 큐와 스택에 들어 있는 문자를 꺼내면서 비교 
#     while qu: #큐에 문자가 남아 있는 동안 반복 
#         if qu.pop(0) != st.pop(): #큐와 스택에서 꺼낸 ㅁ누자가 다르면 회문이 아님 
#             return False
#     return True
# print(palindrome("WoW"))
# print(palindrome("Madam, I'm Adam."))
# print(palindrome("Madam, I am Adam."))

# 문제 13-1 큐와 스택을 이용하지 않고 회문인지 아닌지 판단 하는 알고리즘 

# 주어진 문장이 회문인지 확인(문자열의 앞뒤를 서로 비교)
# 입력: 문자열 s 
# 출력: 회문이면 True, 아니면 False

# def palindrome(s):
#     i = 0          # 문자열의 앞에서 비교할 위치
#     j = len(s) - 1 # 문자열의 뒤에서 비교할 위치
#     while i < j:   # 중간까지만 검사하면 됨
#         # i 위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
#         if s[i].isalpha() == False:
#             i += 1
#         # j 위치에 있는 문자가 알파벳 문자가 아니면 앞으로 이동
#         elif s[j].isalpha() == False:
#             j -= 1
#         # i, j 위치 둘다 알파벳 문자가 있으면 두 문자를 비교하고 다르면 회문이 아님
#         elif s[i].lower() != s[j].lower():
#             return False
#         # i와 j 위치에 두 문자를 비교하고 같으면 다음 비교 대상으로 넘어감
#         else:
#             i += 1
#             j -= 1

#     return True

# print(palindrome("Wow"))
# print(palindrome("Madam, I’m Adam."))
# print(palindrome("Madam, I am Adam."))

# def palindrome(s):
#     x = 0          #앞
#     y = len(s) - 1 #뒤
#     while x < y:   
        
#         if s[x].lower() != s[y].lower():
#             return False
        
#         else:
#             x += 1
#             y -= 1

#     return True

# print(palindrome("Wow"))
# print(palindrome("Madam, I’m Adam."))
# print(palindrome("Madam, I am Adam."))

# 딕셔러니를 이용해 동명이인 찾기 알고리즘
# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: n개의 이름 중 반복되는 이름의 집합

# def find_same_name(a):
#     # 1단계: 각 이름의 등장 횟수를 딕셔너리로 만듦
#     name_dict = {}
#     for name in a:  # 리스트 a에 있는 자료들을 차례로 반복
#         if name in name_dict:     # 이름이 name_dict에 있으면
#             name_dict[name] += 1  # 등장 횟수를 1 증가
#         else:                     # 새 이름이면
#             name_dict[name] = 1   # 등장 횟수를 1로 저장

#     # 2단계: 만들어진 딕셔너리에서 등장 횟수가 2 이상인 것을 결과에 추가
#     result = set()  # 결괏값을 저장할 빈 집합
#     for name in name_dict:  # 딕셔너리 name_dict에 있는 자료들을 차례로 반복
#         if name_dict[name] >= 2:
#             result.add(name)

#     return result

# name = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
# print(find_same_name(name))

# name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(find_same_name(name2))

# 문제 14-1 딕셔너리로 학생 번호에 해당하는 학생 이름 찾기 
def get_name(x_info, y_no):
    if y_no in x_info:
        return x_info[y_no]
    else:
        return "?" 
dic_info = {39: "Justin", 14: "John", 67:"Mike", 105:"Summer"}
print(get_name(dic_info, 39))
print(get_name(dic_info, 9))