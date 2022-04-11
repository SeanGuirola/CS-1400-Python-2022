#For 5-3 use 3- 5 major monthly expenses you have.  For example, car, school,
#food, fun, rent... Your program should get
#your budget and then subtract the sum of your monthly expenses to compute print if for the month you are over budget, equal to budget or under budget. 
#Submit a hand drawn or Raptor flowchart of logic and Python Program which corresponds to flowchart and a test case for a month.

stop = 0 # a conditional that will be used in the while loop to end it
counter =0
budget = float(input("enter your monthly budget: "))
while(stop!=1):
    expense = float(input("Enter your next monthly expense (enter 0 to stop adding expenses):"))
    if(int(expense) == 0):
        stop=1
        break
    else:
        counter += float(expense)


if(counter == budget):
    print("your budget of ", budget, "is equal to your total monthly expenses of ", counter)
elif(budget> counter):
    print("congrats your monthly budget of ", budget, "is greater than your total monthly expenses of ", counter, "by $" , budget-counter )
else:
    print("better luck next month :( your total monthly expenses of ", counter, "is more than you budget of ", budget, "by $", budget-counter)
    
    
