
# CTI-110 
 # M3HW1 - Age Classifier 
 # lEWIS
 # 9/24/2017
 ##The purpose of this program is to output a person's age classification.


#Age is inputed as an integer varaible by user
age = int(input("The person's Age"))

#IF statements provide ranges for age classifications using numerical and logical comparison operators 
def main():
    if age >= 20:
        print("The person is an adult")     
    elif age >= 13 and age< 20:
        print("The person is an teenager")
    elif age >1 and age< 13:
        print("The person is an child")
    else:
        age< 1
        print("The person is an infant")
main()
