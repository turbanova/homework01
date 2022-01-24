t = float(input("John ran today"))
m = float(input("But he has to run"))
i = 0
while t <= m:
    print(f"{t:.2f}", end = " ")
    t = t + t * 0.1
    i = i + 1
    

print(f"{t:.2f}")
print(str(i))

