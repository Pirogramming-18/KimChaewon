studentslist=[]
##############  menu 1
def Menu1(student) :
    #사전에 학생 정보 저장하는 코딩 
    studentslist.append(student)

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
        print("지금 수정한 학생 정보")
        print(studentslist[i])


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
    else:
        break
