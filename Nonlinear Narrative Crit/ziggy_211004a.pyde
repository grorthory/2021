def intro():
    global pets_name
    print("'The Adventure of Ziggs' is a game that simulates what it is like to be my cat (ziggy) on the hunt for a wee mouse on the loose in the maze designed after my house's floor plan. There are several obstacles you might run into while playing ziggy, such as delicious distractions and owners who can't help but scoop you up for cuddles or favors.")
    print("When playing, be sure to respond to questions using CAPITAL LETTERS. I recommend putting caps lock on if you are able to. When responding to the questions the choices for responses are shown in parenthesis in the previous lines.")
    print("The idea for this game came from missing my little guy. Before we begin, what is your pet's name? If you don't have a pet, name someone you are often homesick for.")
    pets_name = raw_input("> ")
    print("Wonderful! Sending an abundance of love to " + pets_name + " <3! Now let's begin!")
    living_room()
    

def living_room():
    print ("you are deep in sleep, you are no longer 'ziggy' the house cat who is snuggled daily and frequently asked to eat bugs, you are a lion.")
    print("you hear rusting and wake from your dream.")
    print("you lazily stretch awake in your cat tree, annoyed at being pulled away from your god-like dream state. it is night time and you are alone in the living room.")
    print("suddenly, you see a mouse scurry from under the couch and right past your cat tree!!!")
    print("you thought you saw it run towards the master bedroom (MB) but you now hear a high pitched scream coming from the kitchen (KT)!")
    print("where would you like to go?")
    
    response = raw_input("> ").lower()
    if "MB" in response:  
        master_bedroom()
    elif "KT" in response:
        kitchen()
    else:
        print ("quit messing around zigs! you are on a mission.")
        living_room()

def kitchen():
    print("you are now in the kitchen, it smells like chili and you are almost distracted....")
    print("you hear the same scream again and it momentarily rips you away from your chili dreams.")
    print("the scream is coming from the laundry room (LDR) through the kitchen, the chili is on the counter (C) and the living room (LR) is back behind you")
    print("where would you like to go?")

    response = raw_input("> ").lower()
    if "LDR" in response:  
        caught_anna()
    elif "C" in response:
        CC()
    elif "LR" in response:
        living_room2()
    else:
        print ("quit messing around zigs! you are on a mission.")
        kitchen()

def caught_anna():
    print("you push through the swinging door into the laundry room. you see your aunt recoiling from the laundry machine in the corner")
    print("she turns her head and sees you. 'ziggy! i need you, can you eat this spider for me?'")
    print("she scoops you and you begrudgingly eat the bug")
    print("you've been scooped, game over.")

    response = raw_input("> ").lower()
    intro()

def CC():
    print("you eat all the chili in the bowl and lose your appetite for mouse...tsk tsk, game over.")
    
    response = raw_input("> ").lower()
    intro()
        
def living_room2():
    print("you find yourself back in the living room")
    print("you originally saw the mouse run towards the master bedroom (MB) but the vermin could be anywhere now...including Sara's & Anna's room (AS)")
    print("where would you like to go?")
    
    response = raw_input("> ").lower()
    if "MB" in response:
        master_bedroom()
    elif "AS" in response:
        anna_sara_room()
    else:
        print ("quit messing around zigs! you are on a mission.")
        living_room2()
        
def master_bedroom():
    global has_head_pats
    print("you enter the master bedroom and have run into bob, whenever you run into bob you recieve free head pats.")
    print("there is no danger of being scooped by bob because he is alergic to you (he still loves you very much though! hence the head pats)")
    print("bob walks out of the room and you scope the scene. would you like to look under the bed (B) or keep looking (KL)?")
    
    response = raw_input("> ").lower()
    if "B" in response:
        under_bed()
    elif "KL" in response:
        continue_looking()
    else:
        print ("quit messing around zigs! you are on a mission.")
        living_room2()
    
def under_bed():
    print("you crawl under the bed, the use of your night vision only aids you in finding loose pringles cans and balled up socks...disappointing")
    
    response = raw_input("> ").lower()
    continue_looking()
    
def continue_looking():
    print("you look all around the room. Crawling under the dresser, peeping into his shoes, and wiggling in between the cushions of a love seat with no success.")
    print("you don't see any signs of movement in the master bedroom. should you investigate the sun room to the back of the living room (SR) or Anna & Sara's room (AS)?")
 
    response = raw_input("> ").lower()
    if "SR" in response:
        sun_room()
    elif "AS" in response:
        anna_sara_room()
    else:
        print("quit messing around zigs! you are on a mission.")
        continue_looking()
    


def anna_sara_room():
    print("you walk through the jack and jill bathroom separating the master bedroom from Anna and Sara's room.")
    print("per usual, your mom (sara) has fallen asleep with candles and music on. it is imperative that you do not wake her because she will most definitely want you to stay!")
    print("do you risk it and poke around her room (RI)? Or do you play it safe and head out to search the sun room (PS)?")

    response = raw_input("> ").lower()
    if "RI" in response:
        caught_sara()
    elif "PS" in response:
        sun_room()
    else:
        print ("quit messing around zigs! you are on a mission.")
        anna_sara_room()
    
def caught_sara():
    print("you walk around her bed to look behind her and anna's pile of books, clothes and assorted knick knacks.")
    print("you step on the spinning machine that makes noise (record player) and the sounds begin to skip irregularly! Sara wakes from her sleep, rubs her eyes and sees you.")
    print("'what are you doing stink?' is the last thing you hear before she scoops you, blows out the candles, and returns to bed with you in her arms.")
    print("you are too comfortable to resist and don't want to hurt her feelings by leaving, game over.")
   
    response = raw_input("> ").lower()
    intro()
    
def sun_room():
    print("you walk past the living room to continue your search.")
    print("on your way into the sun room you hear a scurry of keys across the piano towards the front of the living room!")
    print("would you like to investigate the piano in the living room (P) or continue into the sun room (SR)?")
    
    response = raw_input("> ").lower()
    if "P" in response:
        piano()
    elif "SR" in response:
        sun_room2()
    else:
        print("quit messing around zigs! you are on a mission.")
        sun_room()
    
def sun_room2():
    print("you decide to ignore the sound of the piano that is most definitely a mouse to explore the sun room. nice.")
    print("you look around the old furniture and boxes for storage and come across something even more facinating than a mouse...a hole in the screen window!")
    print("you peep your little head into the hole and wiggle your body through. you are now in the back yard.") 
    print("you think back to your mouse hunt but quickly lose any motivation to return when you lock eyes with a squirrel!")
    print("you chase him all over the yard!")
    print("*swoosh")
    print("*swoosh")
    print("*BAM*")
    print("you slam into the neighbors cat, Marmalade, who is also chasing the squirrel.")
    print("marmalade is a fat, orange, outdoor cat, who is not too fond of you...")
    print("you get hissed at and surrender the chase, slipping back inside to look for a hug")
    print ("sorry little buddy, game over.")
    
    response = raw_input("> ").lower()    
    intro()


def piano():
    print("you sprint to the piano and finally lay eyes on the mouse!!! The mouse sees you and makes a run for it across the strings in the back of the piano")
    print("a symphony of pure chaos!")
    print("*bam")
    print("*bam")
    print("*wham")
    print("*wham")
    print("*SQUEAK*")
    print("you have successfully caught the mouse! what a victory! your bravery and cunning skill is that of a lion young sir, bravo ziggy, bravo!")
    print("now that you have acquired a dead mouse body, what would you like to do with it?")
    print("would you like to, give it to bob (B)? or put it in the chili pot for later (CP)?")
     
    response = raw_input("> ").lower()
    if "B" in response:
        bob()
    elif "CP" in response:
        chilipot()
    else:
        print("quit messing around zigs! you are on a mission.")
        piano()
    
def bob():
    global has_head_pats
    print("you leave a half eaten mouse at the feet of bob who is now on the couch in the living room.")
    print("'whatcha got there buddy?' bob says to you before leaning over to get a closer look at what is by his feat.")
    print("'oh! wow, that's gross - I mean - good job ziggy, thank you lil guy'")
    print("you receive more free headpats and before bob asks you 'how about some celebratory chili?")
    print("all is well in the world of ziggy, game over.")
    
    response = raw_input("> ").lower()
    intro()
    
def chilipot():
    print("you run to the kitchen to store your mouse in the chili pot")
    print("this ingenious plan will ensure that all of this chili belongs to you!")
    print(" *plop! ")
    print("you enjoy your chili until the bowl is clean, absolutely delicious! all is well in the world of ziggy, game over.")
    
    response = raw_input("> ").lower()
    intro()
