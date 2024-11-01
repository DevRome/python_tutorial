unit = input("Is this teperatue in Celsius or Farenheit (C or F) ?")
temp = float(input("Enter a temperature"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"{temp}°F")  

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"{temp}°C") 

else: 
    print(f"{unit} is invalid unit")