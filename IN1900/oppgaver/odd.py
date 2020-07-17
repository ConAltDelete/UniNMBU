n = int(input("shit number: "))
x = 1
o = 0
while x < n and o < n:
    o = 2*x-1
    if o > n:
        break
    print(o)
    x += 1
