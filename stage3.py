with open("input_single.txt", "r") as file:
    lines = file.readlines()
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])
temperature = a * t**2 + b * t + c
print("Temperature at time", t, "is:", temperature, "°C")