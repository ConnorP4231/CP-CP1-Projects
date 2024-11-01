ask = float(input("Enter a number: "))

integer = f"{int(ask):,}"

floating = f"{ask:.4f}"

precent = f"{ask:.2%}"

dollar = f"${ask:,.2f}"

print("Formatted as an integer with commas:", integer)
print("Formatted as a float with 4 decimal places:", floating)
print("Formatted as a percentage:", precent)
print("Formatted as a dollar amount:", dollar)
