#Sean Guirola
#CS 1400
#4/8/22


#If we use 1698 for the test case we know that it will defintely work since it
#it tests every number
initialNum = int(input("Enter the number you want converted: "))

yesNo = input("Please confirm that "+ str(initialNum)+ " is the number you want converted. (answer y/n)")
romanNumArray= []
#a module or method that will add the roman numeral letter num amount of times
numTimes = 0
letter = ""
def appendArray(letter,num):
    i = 0
    for i in range(num):
        romanNumArray.append(letter)

if (yesNo == "y"):
    if((initialNum/1000) != 0):
        numTimes = int(initialNum/1000)
        letter = "M"
        initialNum -= (1000*numTimes)
        appendArray(letter,numTimes)
        
    if((initialNum/500) != 0):
        numTimes = int(initialNum/500)
        letter = "D"
        initialNum -= (500*numTimes)
        appendArray(letter,numTimes)
        
    if((initialNum/100) != 0):
        numTimes = int(initialNum/100)
        letter = "C"
        initialNum -= (100*numTimes)
        appendArray(letter,numTimes)
        
    if((initialNum/50) != 0): 
        numTimes = int(initialNum/50)
        letter = "L"
        initialNum -= (50*numTimes)
        appendArray(letter,numTimes)
        
    if((initialNum/10) != 0):
        numTimes =int(initialNum/10)
        letter = "X"
        initialNum -= (10*numTimes)
        appendArray(letter,numTimes)
        
    if((initialNum/5) != 0):
        numTimes = int(initialNum/5)
        letter = "V"
        initialNum -= (5*numTimes)
        appendArray(letter, numTimes)
        
    if((initialNum/1) != 0):
        numTimes = int(initialNum/1)
        letter = "I"
        initialNum -=(1*numTimes)
        appendArray(letter, numTimes)
    if(len(romanNumArray) > 0):
            print(*romanNumArray)
            romanNumArray.clear()
    else:
        print("number is zero")

    
    

