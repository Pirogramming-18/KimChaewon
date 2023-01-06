
num = 0

while True:
    try:
        num=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        break
    except ValueError:
        print("정수를 입력하세요.")
print(num)