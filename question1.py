numbers = [10, 22, 33, 45, 52, 40, 75]

for n in numbers:
    if n > 50:
        break
    if n % 5 == 0:
        continue
    print(n)