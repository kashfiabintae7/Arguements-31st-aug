def tipcalc(b, tipPerc):
    tp = b * (0.01 * tipPerc)
    return tp

bill = int(input("Enter the Bill: "))
tip = int(input("Enter the Tip Percentage: "))

total = bill + tipcalc(bill, tip)


print(f"Bill : {bill}")
print(f"Tip Pencentage : {tip}%")
print(f"Total Bill : {total}")