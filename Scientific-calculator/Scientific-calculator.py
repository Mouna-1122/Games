import math

while True:
    print("\n========== SCIENTIFIC CALCULATOR ==========")
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (x^y)")
    print("6.  Square (x²)")
    print("7.  Cube (x³)")
    print("8.  Square Root (√x)")
    print("9.  Cube Root (∛x)")
    print("10. Modulus (%)")
    print("11. Floor Division (//)")
    print("12. Percentage")
    print("13. Sine (sin)")
    print("14. Cosine (cos)")
    print("15. Tangent (tan)")
    print("16. Secant (sec)")
    print("17. Cosecant (cosec)")
    print("18. Cotangent (cot)")
    print("19. Inverse Sine (sin⁻¹)")
    print("20. Inverse Cosine (cos⁻¹)")
    print("21. Inverse Tangent (tan⁻¹)")
    print("22. Log Base 10")
    print("23. Natural Log (ln)")
    print("24. Log Base 2")
    print("25. Exponential (e^x)")
    print("26. Factorial")
    print("27. Absolute Value")
    print("28. Ceiling")
    print("29. Floor")
    print("30. Degrees to Radians")
    print("31. Radians to Degrees")
    print("32. Value of π")
    print("33. Value of e")
    print("34. Exit")

    choice = input("\nEnter your choice (1-34): ")

    if choice == "34":
        print("Thank you for using the calculator!")
        break

    elif choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result =", a / b)
        else:
            print("Error! Cannot divide by zero.")

    elif choice == "5":
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result =", a ** b)

    elif choice == "6":
        a = float(input("Enter number: "))
        print("Result =", a ** 2)

    elif choice == "7":
        a = float(input("Enter number: "))
        print("Result =", a ** 3)

    elif choice == "8":
        a = float(input("Enter number: "))
        if a >= 0:
            print("Result =", math.sqrt(a))
        else:
            print("Square root not possible for negative numbers.")

    elif choice == "9":
        a = float(input("Enter number: "))
        print("Result =", a ** (1/3))

    elif choice == "10":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a % b)

    elif choice == "11":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if b != 0:
            print("Result =", a // b)
        else:
            print("Error! Cannot divide by zero.")

    elif choice == "12":
        total = float(input("Enter total value: "))
        percent = float(input("Enter percentage: "))
        print("Result =", (percent / 100) * total)

    elif choice == "13":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == "14":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == "15":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == "16":
        angle = float(input("Enter angle in degrees: "))
        c = math.cos(math.radians(angle))
        if c != 0:
            print("Result =", 1 / c)
        else:
            print("Undefined")

    elif choice == "17":
        angle = float(input("Enter angle in degrees: "))
        s = math.sin(math.radians(angle))
        if s != 0:
            print("Result =", 1 / s)
        else:
            print("Undefined")

    elif choice == "18":
        angle = float(input("Enter angle in degrees: "))
        t = math.tan(math.radians(angle))
        if t != 0:
            print("Result =", 1 / t)
        else:
            print("Undefined")

    elif choice == "19":
        value = float(input("Enter value (-1 to 1): "))
        if -1 <= value <= 1:
            print("Result =", math.degrees(math.asin(value)))
        else:
            print("Invalid input")

    elif choice == "20":
        value = float(input("Enter value (-1 to 1): "))
        if -1 <= value <= 1:
            print("Result =", math.degrees(math.acos(value)))
        else:
            print("Invalid input")

    elif choice == "21":
        value = float(input("Enter value: "))
        print("Result =", math.degrees(math.atan(value)))

    elif choice == "22":
        a = float(input("Enter number: "))
        if a > 0:
            print("Result =", math.log10(a))
        else:
            print("Log undefined for non-positive numbers.")

    elif choice == "23":
        a = float(input("Enter number: "))
        if a > 0:
            print("Result =", math.log(a))
        else:
            print("Log undefined for non-positive numbers.")

    elif choice == "24":
        a = float(input("Enter number: "))
        if a > 0:
            print("Result =", math.log2(a))
        else:
            print("Log undefined for non-positive numbers.")

    elif choice == "25":
        a = float(input("Enter value of x: "))
        print("Result =", math.exp(a))

    elif choice == "26":
        n = int(input("Enter a positive integer: "))
        if n >= 0:
            print("Result =", math.factorial(n))
        else:
            print("Factorial not defined.")

    elif choice == "27":
        a = float(input("Enter number: "))
        print("Result =", abs(a))

    elif choice == "28":
        a = float(input("Enter number: "))
        print("Result =", math.ceil(a))

    elif choice == "29":
        a = float(input("Enter number: "))
        print("Result =", math.floor(a))

    elif choice == "30":
        angle = float(input("Enter degrees: "))
        print("Result =", math.radians(angle), "radians")

    elif choice == "31":
        angle = float(input("Enter radians: "))
        print("Result =", math.degrees(angle), "degrees")

    elif choice == "32":
        print("π =", math.pi)

    elif choice == "33":
        print("e =", math.e)

    else:
        print("Invalid choice! Please try again.")