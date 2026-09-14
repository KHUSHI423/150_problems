if __name__ == "__main__":
    temp = float(input("Enter the temperature : "))
    scale = input("Enter the scale to convert to (F/C/K): ").upper()
    if scale == "C":
        print("temperature in Celsius:", temp)
        f = (temp * 9/5) + 32
        k = temp + 273.15
        print("temperature in Fahrenheit:", f)
        print("temperature in Kelvin:", k)
    elif scale == "F":
        print("temperature in Fahrenheit:", temp)
        c = (temp - 32) * 5/9
        k = c + 273.15
        print("temperature in Celsius:", c)
        print("temperature in Kelvin:", k)
    elif scale == "K":
        print("temperature in Kelvin:", temp)
        c = temp - 273.15
        f = (c * 9/5) + 32
        print("temperature in Celsius:", c)
        print("temperature in Fahrenheit:", f)
    else:
        print("Invalid scale. Please enter F, C, or K.")
    