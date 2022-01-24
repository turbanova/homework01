d = float(input("proceeds"))
c = float(input("costs"))

if d > c:
    print("It`s OK")
    r = (d - c) / d
    print("Your succsess is " + str(r))
    p = int(input("people in your company:"))
    b = (d - c) / p
    print("Everybody has " + str(b))
else:
    print("Not good")
