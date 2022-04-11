#Sean Guirola
#3/30/2022
#CS 1400
#Richard Borrowdale


#Constants (held in an array):
neededIngredients = []
BROWNIES_PER_PAN = 24 #Calculated assuming that you use a 8x12 pan and cut in 2x2in squares
#will use ml since it makes it easier to convert to liters and stuff like that
NORM_BUTTER = 16 #table spoon
NORM_VEGGIE_OIL = 2 # table spoons
NORM_WHITE_SUGAR = 20 # table spooons
NORM_LIGHT_BROWN_SUGAR = 16 # table spoons
NORM_EGGS = 16 #large eggs not in ml (57ml roughly) might want to add a line
            # that reccomends to round up/down to use a whole egg
NORM_VANILLA_EXTRACT = 1 # table spoon
NORM_SALT = 1 #table spoon
NORM_FLOUR = 16 #table spoon
NORM_COCOA_POWDER = 16 # table spoon
NORM_CHOC_CHIP = 14# table spoon
neededIngredients = [NORM_BUTTER, NORM_VEGGIE_OIL, NORM_WHITE_SUGAR,
NORM_LIGHT_BROWN_SUGAR, NORM_EGGS, NORM_VANILLA_EXTRACT, NORM_SALT, NORM_FLOUR,
NORM_COCOA_POWDER,NORM_CHOC_CHIP]

ingredientNames = ["butter", "vegetable oil", "White Sugar", "Light Brown Sugar", "eggs", "Vanila Extract", "sea salt", "All purpose flour", "Cocoa Powder", "chocolate chip"]
#variables will give them 0.0 to declare them as floats

numOfBrownies = float(input ("Enter the Number of brownies you want to make: "))

conversionRate = numOfBrownies/BROWNIES_PER_PAN
if (BROWNIES_PER_PAN%numOfBrownies == 0):
    del neededIngredients [4]
    del ingredientNames[4]
    print(4*conversionRate, "eggs")
for i in range(len(neededIngredients)):                     #using an array is more efficient but I forgot how to check the run-time complexity.
    neededIngredients[i]*=conversionRate
    if (neededIngredients[i] >= 16):
        print(round(neededIngredients[i]/16,2),  ' cups of ' + ingredientNames[i])
    elif (neededIngredients[i]> 2):
        print(round(neededIngredients[i]/2,2), 'oz of ' + ingredientNames[i])
    else:
         print(round(neededIngredients[i],2), ' tablespoons of ' + ingredientNames[i])


     

if((BROWNIES_PER_PAN%numOfBrownies) != 0):    #a check will only round up if it doesn't already call for a whole amount of eggs
    print("________________________________________________________")
    print("However, I'd reccomend using: ") #added this check to because you need to round up or down because you can't have part of an egg
    eggRoundUp = (NORM_EGGS /4) + 1
    conversionRate= (eggRoundUp*4)/NORM_EGGS
    print(eggRoundUp, "eggs")
    del neededIngredients [4]
    del ingredientNames [4]
    for i in range(len(neededIngredients)):
        neededIngredients[i]*=conversionRate
        if(i!= 4):
            if (neededIngredients[i] >= 16):
                print(round(neededIngredients[i]/16,2),  ' cups of ' + ingredientNames[i])
            elif (neededIngredients[i]>2):
                print(round(neededIngredients[i]/2,2), 'oz of ' + ingredientNames[i])
            else:
                 print(round(neededIngredients[i],2), ' tablespoons of ' + ingredientNames[i])
    print(" ")           
    print("ingredients were rounded up to the next nearest whole egg, because you can't cook with just part of an egg")
    
    
    
