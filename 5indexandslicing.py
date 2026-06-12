import pandas as pd

'''
판다스 자료형은 인덱싱을 지원하는 속성인 인덱서를 사용해 인덱싱과 슬라이싱을 할 수 있다.
인덱서는  
🧩 명시적인 인덱스를 기준으로 인덱싱하는 Loc과 (명시적 : 시리즈 혹은 데이터 프레임의 실제 인덱스 의미)
🧩 암묵적인 인덱스를 기준으로 인덱싱하는 iloc (암묵적 : 위치 인덱스 의미)
'''

# S의 인덱스는 [1,3,5,7] , 이처럼 직접 지정하거나 출력했을 때 보이는 인덱스를 명시적 인덱스라고 한다. 
S = pd.Series(["A","B","C","D"], index=[1,3,5,7])
print(S)
# 1    A
# 3    B
# 5    C
# 7    D
# dtype: object


#하지만 파이썬에서 순회 가능한 자료의 요소의 인덱스는 0부터 시작한다고 배웠다. 
# 즉 A의 인덱스는 0, B의 인덱스는 1 => 이러한 위치 인덱스를 암묵적 인덱스라고 한다.
print(S.loc[1]) 
# A

print(S.loc[5:7])
# 5    C
# 7    D
# dtype: object

print(S.loc[5])
# C


'''암묵적 인덱싱 iloc'''
print(S.iloc[0])
# A

print(S.iloc[1:3])
# 3    B
# 5    C
# dtype: object


'''
데이터 프레임의 
인덱싱과 슬라이싱
'''
df = pd.DataFrame(
    {"A":[1,2,3,4], "B":[10,20,30,40],"C":[5,6,7,8]},index=[1,3,5,7]
)
print(df)
#    A   B  C
# 1  1  10  5
# 3  2  20  6
# 5  3  30  7
# 7  4  40  8

'''데이터 프레임의 인덱싱과 슬라이싱은 2차원 ndarray와 유사
df.loc[row,cloumn]
df.iloc[row,column]
'''

print(df.loc[1]) # 인덱스가 1인 행을 출력
# A     1
# B    10
# C     5
# Name: 1, dtype: int64

print(df.loc[5]) # 인덱스가 5인 행을 출력
# A     3
# B    30
# C     7
# Name: 5, dtype: int64

print(df.iloc[0]) # 0번째 위치에 있는 행을 출력
# A     1
# B    10
# C     5
# Name: 1, dtype: int64

print(df.iloc[1]) # 1번째 위치에 있는 행을 출력
# A     2
# B    20
# C     6
# Name: 3, dtype: int64


print(df.loc[1:3]) # ✅ 데이터 프라임을 슬라이싱한 결과도 데이터프레임이다.
#    A   B  C
# 1  1  10  5
# 3  2  20  6

print(df.iloc[0:1])
#    A   B  C
# 1  1  10  5

# ✅ loc은 끝 인덱스를 포함하고 iloc은 포함하지 않는다.



'''
행과 열 함께 인덱싱
'''
print(df.loc[1,"A"]) #1행 A열 출력(명시적)
print(df.loc[3,"B"]) #3행 B열 출력(명시적)

print(df.iloc[0,1]) #0행 1열 출력(암묵적)
print(df.iloc[1,2]) #1행 2열 출력(암묵적)
