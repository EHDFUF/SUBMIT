# 1번문제 : inch -> cm 변환해야함 (참고 : 1인치 = 2.54cm)

cm_from_inch = int(input("inch 단위를 입력하세요: "))

print(f"{cm_from_inch * 2.54}cm 입니다") # 입력값을 문자열에 삽입하기 위해 f-string 사용

# 2번문제 : kg -> 파운드 변환해야함 (참고 : 1kg = 2.20462파운드)

pound_from_kg = int(input("kg 단위를 입력하세요: "))

print(f"{round(pound_from_kg * 2.20462, 1)}pound 입니다")

# 3번문제 : 반지름 r 로 원둘레,넓이 구하기 (이건 참고 안해도 될듯)

radius = int(input("반지름을 입력하세요: "))
pi = 3.14 # 상수 , 파이값은 안변함 

print(f"원의 둘레는 {round(2 * radius * pi, 1)}입니다 \n원의 넓이는 {round(radius ** 2 * pi, 1)}입니다다 ")

# 끝끝 과제끝

