import random
num2 = []
num = random.randint(3, 20)
for i in range(1, 10):
    for j in range(2, 20):
        if num % (i + j) == 0:
            num2.append(i)
            num2.append(j)
result = ''.join(map(str, num2))
print("Число ", num, "Пароль ", result)








