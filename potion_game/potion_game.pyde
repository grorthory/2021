import random

ingredients = ["eye of newt", "toe of frog", "wing of bat", "tongue of dog", "dragon's scale"]
pot = []
ingredients_index = 0

effects0 = ["You sprout a third eye on your forehead!", "Your tongue splits into a fork!", "Your skin begins to ooze slime!", "Gills form on the sides of your face!", "A tail emerges from your back!"]
effects1 = ["Webs form on your feet!", "You begin to leap and bound uncontrollably!", "Your mouth widens to your ears!", "Your tongue grows tenfold!", "You have the sudden urge to eat flies!"]
effects2 = ["Furry wings spring from your back!", "Your teeth sharpen into points!", "Your skin turns ghostly pale!", "You can hear everything!", "Your ears become furry points!"]
effects3 = ["Your nose grows into a snout!", "You fall on all fours!", "Fur sprouts all over your body!", "Your vision fades into black and white!", "You have a sudden hunger for meat!"]
effects4 = ["Scaly wings spring from your back!", "You belch flame uncontrollably!", "Scales grow all over your body!", "Smoke emerges from your nostrils!", "Your blood runs cold!"]
alleffects = [effects0, effects1, effects2, effects3, effects4]

effects =[]

def check_ingredients():
    print("Ingredients remaining:")
    if ingredients == []:
        print("There are no ingredients remaining.")
    else:
        for i in range(len(ingredients)):
            print("-" + ingredients[i])

def input():
    print("")
    input = raw_input(" >").lower()
    return input
print("You are a witch brewing a potion.")
print("There is a bubbling cauldron before you, and ingredients are strewn all about your lair.")
print("All your test animals have long since escaped or became your ingredients, so you will be your own taster.")
def turn():
    check_ingredients()
    if pot == []:
        print("There are no ingredients in the pot.")
    else:
        print("Ingredients in the pot:")
        for i in range(len(pot)):
            print("-" + pot[i])
    response = input()
    ingredient = None
    for i in range(len(ingredients)):
        if ingredients[i] in response:
            ingredient = ingredients[i]
            ingredients_index = i
            break
    if "eat" in response:
        print("I wouldn't eat that if I were you.")
    elif "stir" in response or "mix" in response:
        print("You stir the cauldron as it bubbles.")
    elif "cackle" in response or "laugh" in response:
        print("You cackle madly.")   
    elif ingredient != None:
        pot.append(ingredient)
        effects.append(alleffects[ingredients_index][random.randint(0, 4)])
        ingredients.remove(ingredient)
        print("You add the " + ingredient + " to the pot.")
    elif "drink" in response:
        print("You drink the potion.")
        if pot == []:
            print("The potion tastes like plain water. Try adding some ingredients.")
        else:
            for i in range(len(effects)):
                print(effects[i])
            print("You admire your new form before departing in search of peasants to terrorize.")
            print("THE END")
            exit()
    elif "remove" in response or "take" in response:
        print("You reach in, but the heat of the cauldron forces your hand to withdraw.")
    else:
        print("You can't do that.")
        print("Ingredient names must be typed out fully.")
    turn()
turn()
