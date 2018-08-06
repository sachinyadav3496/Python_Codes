def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32
    result = "It's "+str(celsius2fahrenheit(t)) + " degree!"
    return result

print(temperature(20))
