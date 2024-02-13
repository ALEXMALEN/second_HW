meters = float(input("Enter meter quantity: "))

choice = input("Choose an operation (miles, inches or yards): ")

if choice == "miles":
    result = meters * 0.000621371
    print("Quantity miles: ", result)
elif choice == "inches":
    result = meters * 39.3701
    print("Quantity inches: ", result)
elif choice == "yards":
    result = meters * 1.09361
    print("Quantity yards: ", result)
else:
    print("Incorrect operation selection. Please select 'miles', 'inches' or 'yards'.")