import pandas as pd

# 중첩 배열과 인덱스, 칼럼을 입력해서 데이터 프레임
df1=pd.DataFrame([[1,2],[3,4]], columns=["A","B"],index=["x","y"])
print(df1)
''' 
출력결과

   A  B
x  1  2
y  3  4
'''

#데이터만 입력해서 데이터 프레임 만들기
df2 = pd.DataFrame([[1,2],[3,4]])
print(df2)
'''
   0  1
0  1  2
1  3  4
'''

#딕셔너리를 이용한 데이터 프레임 생성
df3 = pd.DataFrame({"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]}, index=["x","y","z"])
print(df3)
'''
   A  B  C
x  1  4  7
y  2  5  8
z  3  6  9

'''


# 데이터 프레임 속성
''' 데이터는 values로 인덱스는 index 속성으로 접근, 칼럼은 columns'''
print(df1.values)
#[[1 2]
#  [3 4]]

print(df1.index)
# Index(['x', 'y'], dtype='object')

print(df1.columns)
#Index(['A', 'B'], dtype='object')

'''시리즈와 마찬가지로 데이터는 ndarray자료형이며, 인덱스와 칼럼은 Index 자료형'''



'''

'''

