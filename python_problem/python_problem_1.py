import math

num = 0
count=0

while True:
    try:
        num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if num<1 or num>3:
            raise IndexError
    except ValueError:
        print("정수를 입력하세요.")
    except IndexError:
        print("1,2,3 중 하나를 입력하세요") 
    
    for i in range(0,num):
        print("playerA : {}".format(count+1))
        count+=1
    print(count)