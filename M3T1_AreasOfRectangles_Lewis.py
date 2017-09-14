# M3T1 Areas of Rectangles

# Psudo code
#Input
# Input the length and width of rectangle 1.
#Input the length and width of rectangle 2.

#Process
# Calculate the area of rectangle 1.
# Calculate the area of rectangle 2.
#Determine which rectangle "rectangle 1 or rectangle 2"has the greater area or is the same

#Get the dimenesions of rectangle 1.
length1 = int(input("Enter the Length of rectangle1:"))
width1 = int(input("Enter the width of rectangle1:"))

#Get the dimensions of rectangle 2.
length2 = int(input("Enter the length of rectangle 2:"))
width2 = int(input("Enter the wioth of rectangle 2:"))

# Calculate teh areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2         

#Determine which has the greater area.
if area1 > area2:print("Rectangle 1 has the greater area.")
elif area2 > area1:print("Rectangle 2 has the greater area.")
else:print('Both have the same area.')







             
                   
