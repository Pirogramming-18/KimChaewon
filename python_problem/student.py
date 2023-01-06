#함수 이름은 변경 가능합니다.

studentslist=[]
##############  menu 1
def Menu1(student) :
    #사전에 학생 정보 저장하는 코딩 
    studentslist.append(student)


##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(studentslist)):
        avg=(studentslist[i][1]+studentslist[i][2])/2
        if avg>=90:
            studentslist[i].append("A")
        elif avg>=80:
            studentslist[i].append("B")
        elif avg>=80:
            studentslist[i].append("c")
        else:
            studentslist[i].append("D") 
        avg=0   

##############  menu 3
def Menu3() :
    #출력 코딩
    print("-----------------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-----------------------------------")

    for student in studentslist:
            print("{0}\t{1}\t{2}\t{3}".format(student[0],student[1],student[2],student[3]))


##############  menu 4
def Menu4(number):
    #학생 정보 삭제하는 코딩
    del studentslist[number]


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        try:
            student =list(input("Enter name mid-score final score:").split())
            if len(student)!=3:
                raise IndexError
            for i in range(len(studentslist)):
                if studentslist[i][0]==student[0]:
                    raise NameError
            student[1]=int(student[1])
            student[2]=int(student[2])
            if student[1]<0 or student[2]<0:
                raise ValueError
        except IndexError: #개수 3개 에러
            print("Num of data is not 3!")
        except NameError: #이미 존재하는 이름
            print("Already exist name!")
        except ValueError: #정수가 아님
            print("Score in mt positive integer!")
        else:
            Menu1(student)

    elif choice == "2" :
        try:
            if len(studentslist)==0:
                raise IndexError
        except IndexError:
                print("No student data!") 
        else:
            Menu2()
            print("Grading to all students")
            
    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        try:
            num = len(studentslist)
            if num==0:
                raise IndexError
            else:
                for i in range(num):
                    if len(studentslist[i]) !=4:
                        raise ValueError
        except ValueError:
            print("There is a student who didn't get grade.")
        except IndexError:
                print("No student data!") 
        else:
            Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

        try:
            temp=0
            name = input("Enter the name to delet: ")
            num = len(studentslist)
            if num==0:
                raise IndexError
            else:
                for number in range(num):
                    if studentslist[number][0] == name:         
                        break
                    else:
                        temp+=1
                if temp==num:
                    raise ValueError
        except ValueError:
            print("Not exist name!")
        except IndexError:
                print("No student data!") 
        else:
            Menu4(number)
            print("{} student information is deleted.".format(name))

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit porgram!")
        break


    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")