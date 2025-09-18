"""
2개 이상의 자연수(양의 정수)를 입력받고 다양한 연산을 선택하여 계산합니다.
"""
ops_name = ["차원(길이)", "합", "교대합", "제곱합", "벡터길이"]  
num_ops = len(ops_name)
num_list = []
choose_op = "연산 종류(0~"+str(num_ops-1)+") 중에서 선택하세요: "
print("연산 종류")
for i in range(num_ops):
    print(f"{i} : {ops_name[i]}")
def calc():
    pass
if __name__ == "__main__":
    calc()