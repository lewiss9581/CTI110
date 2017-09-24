# The purpose of this program is to calculate user input of their number grades and then output the letter grade
# Lewis.

# The def main or code being excuted later sets the following variables: A_score = 90, B_score = 80, C_score = 70, D_score = 60, F_score = 50,
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

# The user input a integer.
score = int(input('Enter grade'))

# The code then calculates the letter grade of the user using: 90 >= A_score, 80 >= B_score, 70 >= C_score, 60 >= D_score, 50 >= F_score 
def main():
   if score >=A_score:
        print('Your grade is: A')
   elif score >=B_score:
        print('Your grade is: B')
   elif score >=C_score:
        print('Your grade is: C')
   elif score >=D_score:
        print('Your grade is: D')
   else:
        print('Your grade is: F')

# The program then excutes by printing a letter grade as a result of its evaluation of the if statements. 
main()




 

