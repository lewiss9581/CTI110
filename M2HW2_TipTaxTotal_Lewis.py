# CTI-110 
# M2HW2 - Tip Tax Total 
# Lewis 
# 09/10/2017

#variables
foodcost = float(input("Foodcost"))
salestax = 0.07
tipamount = .18
foodcostsalestax = foodcost * salestax + foodcost
foodcostsalestaxtipamount = tipamount * foodcostsalestax + foodcostsalestax
totalcost = foodcostsalestax * tipamount + foodcostsalestax

#Calculation process
print( "foodcost with sales tax is:")
print(foodcost * salestax + foodcost)
print("With 18% tip")
print(foodcostsalestax * tipamount )
print("total cost")
print(foodcostsalestax * tipamount + foodcostsalestax)



