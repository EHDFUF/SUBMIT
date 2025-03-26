# 16진수변환함수 hex()
# 8진수변환함수 oct()
# 2진수변환함수 bin()

number_decide = int(input("입력 진수 결정(16/10/8/2) : "))

if number_decide == 16 or number_decide == 10 or number_decide == 8 or number_decide == 2:

    number_input = input("값 입력 : ")
    number_for_convert = int(number_input, number_decide) #hex(),oct(),bin() 함수를 사용하기 위해 number_input을 10진수 형태로 전환

    print(f"16진수 ==> {hex(number_for_convert)}")
    print(f"10진수 ==> {number_for_convert}")
    print(f"8진수 ==> {oct(number_for_convert)}")
    print(f"2진수 ==> {bin(number_for_convert)}")

else:
    print("16/10/8/2 중의 숫자로 작성하세요")


