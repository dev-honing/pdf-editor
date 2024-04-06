# test.py

n = int(input("숫자 범위를 입력하세요: ")) # 사용자로부터 숫자 범위를 입력받음
print(f"1부터 {n}까지의 숫자 중에서 홀수/짝수를 판별합니다.")

for i in range(1, n+1): # 1부터 n까지 반복
    if i % 2 == 0:
        print(f"{i}은(는) 짝수입니다.")
    else:
        print(f"{i}은(는) 홀수입니다.")