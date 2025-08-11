def calculate_temperature(a, b, c, t):
    return a * t**2 + b * t + c
temp = calculate_temperature(-0.5, 3, 20, 4)
print("Temperature:", temp, "°C")