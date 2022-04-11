#Sean Guirola
#4/8/22
#CS 1400

#INSTRUCTIONS
#--------------
#Book Club Points
#Serendipity Booksellers has a book club that awards points to its customers
#based on the number of books purchased each month. The points are awarded as follows:
#-If a customer purchases 0 books, he or she earns 0 points.
#-If a customer purchases 1 book, he or she earns 5 points.
#-If a customer purchases 2 books, he or she earns 15 points.
#-If a customer purchases 3 books, he or she earns 30 points.
#-If a customer purchases 4 or more books, he or she earns 60 points.
#
#Design a program that asks the user to enter the number of books that he
#or she has purchased this month and displays the number of points awarded.

end = 0 #used as a boolean in a while loop


while(end!=1):
    booksPurchased = int(input("Enter the number of books purchased this month: "))
    if(booksPurchased == 0):
        print("you have 0 points")
        end=1
    elif(booksPurchased == 1):
        print("you have 5 points")
        end =1
    elif(booksPurchased == 2):
        print("you have 15 points")
        end =1
    elif(booksPurchased == 3):
        end = 1
        print("you have 30 points")
        end = 1
    elif(booksPurchased >= 4):
        print ("you have 60 points")
        end =1
    else:
        print("enter a non negative number")
