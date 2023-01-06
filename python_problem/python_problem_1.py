import math

num = 0
count=0
def playerInput():
    while True:
        try:
            num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if num<1 or num>3:
                raise IndexError
            return num
        except ValueError:
            print("정수를 입력하세요.")
        except IndexError:
            print("1,2,3 중 하나를 입력하세요") 

while True:
    inputA=playerInput()
    for i in range(inputA):
        print("playerA : {}".format(count+1))
        count+=1
    inputB=playerInput()
    for i in range(inputB):
        print("playerB : {}".format(count+1))
        count+=1    
    print(count)