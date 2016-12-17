mealCost = input()
tipPercent = input()
taxPercent = input()

tip = (float(mealCost) * int(tipPercent))/100
tax = (float(mealCost) * int(taxPercent))/100
totalCost = round(float(mealCost) + float(tip) + float(tax))
print ("The total meal cost is " + str(totalCost) + " dollars.")