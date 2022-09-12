#python program using a function

def SI(x,y,z):
    s = (x * y * z) / 100
    return s




p = float(input("Enter Principal amount :\n"))
I = float(input("Enter Interest Rate :\n"))
t = float(input("Enter time period :\n"))

a = SI(p,I,t)
print(a)


