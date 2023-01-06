import random
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


def brGame(player,outher,inputs):
    a=count
    for i in range(inputs):
        print("{0} : {1}".format(player,(a+1)))
        a+=1
        if a==31:
            print(outher," win!")
            break
    return a

while count<31:
    inputs=playerInput()
    count=brGame("player","computer",inputs)
    if count>=31:
        break
    inputs=random.randrange(1,4)
    count=brGame("computer","player",inputs)
    if count>=31:
        break