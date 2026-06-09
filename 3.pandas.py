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

