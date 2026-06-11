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


# 현실적인 데이터 프레임 생성 방법
print("################################")
msg_list = ["numpy","pandas","matplotlib"] #메세지 목록 정의
data = [] #연산결과 저장할 변후 리스트로 초기화
for msg in msg_list: # 데이터 프레임의 행을 만듬
      record=[msg]
      for x in ["a","p","n"]:
         record.append(msg.count(x)) #내부 for문을 통해 들어갈 데이터 (각 알파벳이 몇 회 등장했는지설정)
      data.append(record)
data = pd.DataFrame(data, columns=["message","a","p","n"]) #중첩 리스트인 데이타를 데이터 프레임으로 바꿈. 
print(data)    
'''
      message  a  p  n
0       numpy  0  1  1
1      pandas  2  1  1
2  matplotlib  1  1  0

'''
