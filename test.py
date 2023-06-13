import random

numbers = list(range(1, 24))  # 1부터 23까지의 번호를 리스트로 생성

random.shuffle(numbers)  # 번호를 무작위로 섞음

num_groups = 6  # 모둠의 개수를 6으로 설정

group_size = len(numbers) // num_groups  # 모둠 크기 계산
remainder = len(numbers) % num_groups  # 남는 번호 처리를 위한 나머지 계산

groups = []
start = 0

for i in range(num_groups):
    if i < remainder:
        end = start + group_size + 1  # 남는 번호가 있는 경우 모둠 크기를 1 증가시킴
    else:
        end = start + group_size
    groups.append(numbers[start:end])
    start = end

print("편성된 모둠:")
for group in groups:
    print(group)
