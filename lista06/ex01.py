v = []
neg = 0

for i in range(0, 10):
    num = int(input(f'numero {i + 1}°: '))
    v.append(num)
    if num < 0:
        neg += 1

print(v)
print(f'{neg} negativos')