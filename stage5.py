def calculate_temperature(a, b, c, t):
    return a * t**2 + b * t + c
with open("input_multiple.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        a, b, c, t = map(float, parts)
        temp = calculate_temperature(a, b, c, t)
        print(f"For a={a}, b={b}, c={c}, t={t} → Temperature = {temp:.2f} °C")