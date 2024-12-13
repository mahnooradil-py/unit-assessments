def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    conversion_type = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()
    temperature = float(input("Enter the temperature value: "))

    if conversion_type == 'C':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif conversion_type == 'F':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid conversion type. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
