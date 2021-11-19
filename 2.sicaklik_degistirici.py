print("-" * 30)
print("1 - celsius to fahrenheit")
print("2 - fahrenheit to celsius")
print("-" * 30)

choice = input("Your choise (1/2): ")

if choice == "1":
    print("\n# celsius to fahrenheit")
    celcius = float(input("Degree to convert: "))
    fahrenheit = (celcius * 1.8) + 32
    print("{} degree celcius is equal to {} degree fahrenheit".format(celcius,fahrenheit))

elif choice == "2":
    print("\n# fahrenheit to celsius")
    fahrenheit = float(input("Degree to convert: "))
    celcius = (fahrenheit - 32) /1.8
    print("{} degree fahrenheit is equal to {} degree celcius".format(fahrenheit,celcius))
else:
    print("Congratulations! You hacked the super-program.")