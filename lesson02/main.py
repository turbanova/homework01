s = int(input("Введите время в сек"))
m = int(s / 60)
h = int(m / 60)

print(f"Time is {(h % 60):02}:{(m % 60):02}:{(s % 60):02}")