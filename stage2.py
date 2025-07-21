a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time (t): "))
T = a * t ** 2 + b * t + c
print(f"Temperature at {t} hour is {T}°C")