#Module 4 Lab-4
#Jose Ochoa
#3/10/2024
#This program calculated bounes for the store and employees based on sales

#declare local variables
mothlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0

#This code gets the monthly sales
monthlySales = float(input('Enter this month sales '))

#This code determines the store bonus

if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >=80000:
  storeAmount = 3000
else: storeAmount = 0

#This code gets the percent of increase in sales
salesIncrease =float(input('Enter percent of sales increse '))

salesIncrease = salesIncrease / 100

#This code determines the employee bonus
if salesIncrease >= .05:
  empAmount = 75
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
  empAmount = 40
else: empAmount = 0

#This code prints the bonus information
print('--The store bonus amount is $', storeAmount)
print('--The employee bonus amount is $', empAmount)
if(storeAmount == 6000) and (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible!')
