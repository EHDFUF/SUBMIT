computing_number = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))

if computing_number == 1:

    result = input("*** 수식을 입력하세요 : ")
    print(f"{result} 결과는 {eval(result)}입니다")

elif computing_number == 2:

    starting_number = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    finishing_number = int(input("*** 두 번째 숫자를 입력하세요 : "))

    result = 0
    
    for  sumed_number in range(starting_number, finishing_number+1):

        result += sumed_number

    print(f"{starting_number}+...+{finishing_number}는 {result}입니다")

else:
    print("1 또는 2로만 입력해야 합니다!")
