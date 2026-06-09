import pandas as pd
#pandas

'''
판다스의 대표적인 자료형
1차원 배열 : 시리즈(Series)
2차원 배열 : 데이터프레임(DataFrame)

두 자료형 모두 인덱스와 데이터로 구성된다. 
판다스의 자료형은 ndarray에서 사용하는 메서드 혹은 속성 대부분을 사용할 수 있다.
판다스의 인덱스는 딕셔너리의 키처럼 다양한 값을 사용할 수 있다.
'''

#시리즈 생성
s1 = pd.Series([1,2,3], index=["A","B","C"])
print(s1)
'''
인텍스 데이터
A    1
B    2
C    3
dtype: int64
이처럼 시리즈의 데이터는 ndarray이므로 모든 요소의 자료형이 같게 설정됨
시리즈의 자료형은 astype 메서드를 사용해서 변환
'''

s1 = s1.astype(float)
print(s1)
'''
인텍스 데이터
A    1.0
B    2.0
C    3.0
dtype: float64
'''

#시리즈 - 인덱스를 생성하지 않으면 range로 자동으로 설정
s2 = pd.Series([10,20,30])
print(s2)
'''
인텍스 데이터
0    10
1    20
2    30
dtype: int64
'''

#딕셔너리를 이용한 시리즈 생성
s3 = pd.Series({"A":1, "B":2, "C":3, "D":4})
print(s3)
'''
인텍스 데이터
A    1
B    2
C    3
D    4
dtype: int64
'''
