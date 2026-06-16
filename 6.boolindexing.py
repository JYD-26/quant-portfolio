import pandas as pd
import numpy as np

'''
부울 배열을 이용한 인덱싱
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
print("**********************")

cond = df["C"]%2 == 0
print(cond)
# 1    False
# 3     True
# 5    False
# 7     True
# Name: C, dtype: bool
print("**********************")

print(df.loc[cond])
#    A   B  C
# 3  2  20  6
# 7  4  40  8
'''true 인 데이터 프레임만 출력해 준다'''


print("**********************")
print(df.loc[df["A"] <= 3, ["A","C"]])
#    A  C
# 1  1  5
# 3  2  6
# 5  3  7
'''A 컬럼이 3이 하인 행과 A,C 컬럼을 필터링 한 것'''


# 인덱싱을 위해 자주 사용하는 메서드 isin

print("**********************")
print(df["B"].isin([30,20]))
# 1    False
# 3     True
# 5     True
# 7    False
# Name: B, dtype: bool
print("********* isin을 활용하여 bool을 인덱스로 *************")
print(df.loc[df["B"].isin([30,20])])