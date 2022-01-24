n = input("Введите число")

m = 0
while m < len(n):
    d = int(n[m])
    if d > m:
        m = d

print(str(d))
