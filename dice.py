import random

noofdie = int(input("Enter number of dice to roll: "))
noofside = int(input("Enter number of sides: "))

results = []

for i in range(noofdie):
  roll = random.randint(1, noofside)
  results.append(roll)
  print("Roll", i+1, ":", roll)

print("Total:", sum(results))



