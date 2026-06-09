# 손에 잡히는 퀀트 투자 with 파이썬

'''
lamda 함수
:을 기준으로 왼쪽에는 인자를 오른쪽에는 출력을 정의
'''

minus = lambda x,y: x-y

print(minus(2,3))
print(minus(7,3))


'''
클래스
:을 기준으로 왼쪽에는 인자를 오른쪽에는 출력을 정의

__init__ 은, 인스턴스 생성시점 자동 호출
'''


class Stock:
    def __init__(self, name, market="kospi"):
        #market으로 값이 없으면 기본값으로 kospi
        self.name = name
        self.market = market
        
        
samsung = Stock("삼성전자","코스피")
print(samsung.name,samsung.market) 

samsung.name ="현차"
print(samsung.name)


class calculator:
    def __init__(self, value):
        self.value = value
        
    def add_ver1(self, input_value):
        # input_value를 더해 value 속성 업데이트하는 메서드 정의
        self.value += input_value
        
    def add_ver2(self, input_value):
        # input_value를 더한 값을 반환하는 메서드 정의
        return self.value + input_value
    
a = calculator(10)
b = calculator(10)

print(a.add_ver1(5)) # return 없는 메서드로 반환 None
print(b.add_ver2(5)) # return 있는 메서드
print(a.value) 
print(b.value)


# 예외 처리
try:
    a = 6/0
    print(a)
except:
    print("0으로 나눌 수 없다")