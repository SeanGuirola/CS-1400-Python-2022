#Sean Guirola
#3/25/2022
#Lab 1-6 Pedometer
from datetime import date
import datetime # allows getting the actual day in integer representation
import calendar # allows getting the actual day in a string format
curentDate = date.today()
arrayIndex = 0
x=1
backToTop= 1 #this will be used in a while(true) boolean loop possibly a nested loop?

totalStep = int(input("Enter Total Number of Steps Taken Today: "))
milesWalked = totalStep/2000
kcalBurnt = milesWalked * 65
print ("Today is: ", calendar.day_name[curentDate.weekday()], " and you walked", milesWalked, " miles",", and burnt", kcalBurnt, " calories")
recordOfKcal = [kcalBurnt]
recordOfStep = [totalStep] #an array... er 'list' (because python is dumb like that and doesn't just call it an array) that holds total steps per day
recordOfMiles = [milesWalked]
while(bool(x)):
    anotherDay = input("Do you want to add another day? (enter y/n)") 
    if (anotherDay == "y"):  
        totalStep = int(input("Enter Total Number of Steps Taken: "))
        milesWalked = totalStep/2000
        kcalBurnt = milesWalked * 65
        recordOfKcal.append(kcalBurnt)
        recordOfStep.append(totalStep)
        recordOfMiles.append(milesWalked)
    else:
        x=0
while(bool(backToTop)):
    yesNo = input("Do you want to check the records for the last week? (enter y/n)")
    if (yesNo == "y"):
        dayOfWeek = int(input("enter the day that you are checking in terms of an integer with the first day being represented by the value 0"))
        if(dayOfWeek < len(recordOfKcal)):    #adds a check to avoid Index Errors
            print(recordOfKcal[dayOfWeek], " calories burnt")
            print(recordOfStep[dayOfWeek], " steps taken")
            print(recordOfMiles[dayOfWeek], " miles walked")
            backToTop = 0
        else:
            print("There is no data recorded for this day going back to start :(")
            
    elif((yesNo != "y") and (yesNo != "n")): #had an error here where I used && comparison kinda got a little mad here that its not && instead its 'and'
        print("Please answer with 'y' for yes and 'n' for no")
    else:
        backToTop=0
        
yesNo = input("Do You want to clear the records? (enter y/n)")
if (yesNo == "y" ):
    recordOfKcal.clear()
    recordOfStep.clear()
    recordOfMiles.clear()



    
    
