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

def brGame(player,outher):
    a=count
    input=playerInput()
    for i in range(input):
        print("{0} : {1}".format(player,(a+1)))
        a+=1
        if a==31:
            print(outher," win!")
            break
    return a

while count<31:
    count=brGame("playerA","playerB")
    if count>=31:
        break
    count=brGame("playerB","playerA")
    if count>=31:
        break