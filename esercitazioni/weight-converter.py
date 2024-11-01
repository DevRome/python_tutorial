# weight convertr

weight = float(input("Enter our weight"))
unit = input("Kilograms or Pounds? (K or L)")

if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight / 2.205
else:
    print(f"Unit {unit} was not a valid one")

label = "K" if unit == "L" else "L" # ternary
print(f"Your weight is: {weight} {label}" )