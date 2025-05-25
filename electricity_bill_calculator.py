
expenses_input = "12.0, 15.0, 10.0, 13.0, 12.5, 11.0, 14.0"
expenses = [float(x.strip()) for x in expenses_input.split(",")]

average = sum(expenses) / len(expenses)

print(f"O‘rtacha harajat: ${average:.2f} (twelve dollars and sixty-four cents, двенадцать долларов шестьдесят четыре цента)")
