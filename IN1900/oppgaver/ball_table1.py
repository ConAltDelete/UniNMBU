
g = 9.81
v0 = float(input("Shit"))

for t in range(0,(int(round((2*v0)/g)))):
    y = (v0*t)-(0.5*g*t**2)
    print("t={},y={}".format(t,y))
