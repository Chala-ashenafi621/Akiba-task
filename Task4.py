# TASK 4 — Temperature Station
celsius = float(input("Temperature: "))

fahrenheit = (celsius * 9 / 5) + 32
print("\nCelsius:", celsius, "°C")
print("Fahrenheit:", fahrenheit, "°F")


fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))

celsius = (fahrenheit_input - 32) * 5 / 9

print("Fahrenheit:", fahrenheit_input, "°F")
print("Celsius:", celsius, "°C")