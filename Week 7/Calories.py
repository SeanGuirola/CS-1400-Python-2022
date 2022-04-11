#Sean Guirola
#CS 1400
#
#----------------Instructions:---------------------------
#2. Calories Burned
#Running on a particular treadmill you burn 3.9 calories per minute.
#Design a program that uses a loop
#to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
#----------------------------------------------------------------------

KCAL_PER_MIN = 3.9
minutes= 10
for i in range(5):
    print(KCAL_PER_MIN*minutes, "have been burnt in ", minutes, " minutes")
    minutes+=5
