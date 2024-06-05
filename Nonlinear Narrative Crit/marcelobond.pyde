car = False
has_bag = False
drank = False
drugged = False
drunk = False

def intro():
    global name
    print("Hello and welcome to my Friday Night simulation!")
    print("What is your name?")
    name = raw_input("-->").lower()
    print("happy friday " + name + "!")
    print("your friends are calling to make plans for the night.")
    print("you promised them you would go out tonight but you have a midterm on monday you really need to study for.")
    intro2()
    
def intro2():
    print("So what's the move?")
    response = raw_input("-->").lower()
    if "out" in response or "go" in response:
        going_out()
    elif "stay" in response or "study" in response:
        print("Are you sure? You could really use a night off.")
        response = raw_input("-->").lower()
        if "yes" in response or "im sure" in response:
            print("Ok, but are you actually going to study?")
            response = raw_input().lower()
            if "yes" in response:
                desk()
            elif "no" in response:
                couch()
            else:
                print("huh?")
                intro2()    
    else:
        intro2()

def going_out():
    global has_bag
    print("Someone is throwing a small kickback nearby but all your friends to go to this club downtown.")
    response = raw_input("-->").lower()
    if "party" in response or "kickback" in response:
        transb()
            
    elif "club" in response or "downtown" in response or "friends" in response:  
        print("You only have room in your pockets for your phone and wallet. Do you bring your bag?") 
        response = raw_input().lower()
        if "yes" in response or "sure" in response or "bag" in response:
            print("smart")
            has_bag = True
            transc()
        elif "no" in response:
            print("You only really need those things anyway.")
            transc()
        else:
            print("sorry?")
            going_out()    
    else:
        intro2()
        
def transb():
    global car
    print("How are you getting there?")
    response = raw_input("-->").lower()
    if "walk" in response or "walking" in response:
        print("sounds good. looks like its only a few blocks")
        party()
    elif "drive" in response or "car" in response or "driving" in response:
        print("dope. looks close.")
        car = True
        party()
    elif "bus" in response or "train" in response:
        print("Might take a bit but lets go!")
    elif "uber" in response or "lyft" in response:
        print("expensive but beats walking i guess.")
        party()
    else:
        print("sorry, what?")
        party()
                                 
def transc():
    global car
    print("How are you getting there?")
    response = raw_input("-->").lower()
    if "walk" in response or "walking" in response:
        print("not sure that's the best choice.")
        transc()
    elif "drive" in response or "car" in response or "driving" in response:
        print("dope. looks close.")
        car = True
        club()
    elif "bus" in response or "train" in response:
        print("Might take a bit but lets go!")
        club()
    elif "uber" in response or "lyft" in response:
        print("oof. expensive but beats walking i guess.")
        club()
    else:
        print("sorry, what?")
        transc()
                     
  
     
def couch():
    print("looks like your're not the only one staying in tonight.")
    print("You're sitting on the couch watching a movie and your roomate asks if you want to go outside and smoke.")
    print("So? What do you do?")
    response = raw_input("-->").lower()
    if "outside" in response or "smoke" in response:
        print("It's been a minute since you last smoked. you got far too high and fell asleep on the couch")
        print("sleep tight")
    elif "stay" in response or "movie" in response:
        print("movie too good to pause?")
        response = raw_input("-->").lower()
        sleepcouch()                                                                                                                                                                                                                                                                                                                                    
def desk():
    print("so you're really spending your friday night studying for your midterm huh?")
    print("at least you'll be prepared.")
def club():
    global drank
    print("  ")
    print("You made it to the club!")
    if has_bag == False:
        print("Shit! you left your ID in your bag")
        print("Deffinetly not getting into the club without your ID.")
        noclub()

    if has_bag == True:
        print("are you drinking tonight?")
        response = raw_input("-->").lower()
        if "yes" in response or "of course" in response or "absolutely" in response or "yea" in response:
            print("Why else go to the club am i right??")
            drank = True
            dancefloor()
        elif "no" in response or "not" in response:
            print("good idea. cant forget you drove everyone here.")
            drank = False
            dancefloor()
        else:
            print("sorry?")
            club()
    
def sleepcouch():
    print("The movie must not be that good because you just woke up to your roomates coming home and the credits rolling on the screen.")    
    print("You get up and slowly make your way to bed.")
    print("sleep tight")
   
def dancefloor():
    global drugged
    print("You and all your friends have been dancing for a bit and you see someone you met here the weekend before. Do you go over and dance with them or stay with your friends?")
    response = raw_input("-->").lower()
    if "dance" in response or "go" in response:
        print("Alrightttt. You danced your way over to them and they offer to buy you a drink.")
        print("do you accept?")
        response = raw_input("-->").lower()
        if "drink" in response or "yes" in response or "accept" in response:
            drug()
        elif "no" in response:
            print("smart move, you hardly know this person.")
            print("lets go back to your friends.")
            dancefloor2()
        else:
            print("what was that?")
            dancefloor()
    elif "stay" in response or "friends" in response:
        dancefloor2()
    else:
        print("sorry")
        dancefloor()
            
            
              
def noclub():
    print("it's already after 11 so some people are gonna call it a night.")       
    print("but your friend who lives near by invited everyone to go to their place for a kickback since yall couldnt get into the club.")
    print("what do you want to do?")
    response = raw_input("-->").lower()
    if "home" in response or "call it a night" in response:
        print("let's go the hell home then what are you wanting for?")
        home()   
    elif "friends house" in response or "stay out" in response:
        friendshouse()
    else:
        print("sorry?")
        noclub()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

def home():
    print("Let's go home!")
    if drank == True and car == True:
        hospital()
    elif drank == False:
        print("you made it home safe! time for a late night snack and then bed. sleep tight.") 
    elif drank == True and car == False:
        print("dont forget you dont have your car and the busses arent running so you'll have to take an uber.")
        print("")
        print("you made it home safe! time for a late night snack and then bed. sleep tight.") 
    else:
        print("sorry?")
        home()
        
                        
def party():
    print("looks like more of a party than a kickback if you ask me...")
    print("you walk into the house, there are people playing flip cup in the dinning room as well as people standing around the living room and drinks are in the kitchen.")
    print("where to?")
    response = raw_input("-->").lower()
    if "flip cup" in response or "dinning room" in response or "game" in response or "play" in response:
        drank = True
        flipcup()
    elif "kitchen" in response or "drink" in response:
        kitchen()
    elif "living room" in response:
        livingroom()
    else:
        print("sorry?")
        party()

        
def dancefloor2():
    print("You made it back to your friends and they're all just about ready to call it a night.")
    print("Do you want to stay or head out with your friends?")
    response = raw_input("-->").lower()
    if "stay" in response:
        print("your friends left")
        
    elif "go" in response or "friends" in response or "leave" in response:
        print("a couple of your friends are wanting to go to a party nearby but a few are heading home for the night.")
        print("what's your move?")
        response = raw_input("-->").lower()
        if "home" in response:
            home()
        elif "party" in response or "friends" in response:
            party()
        else:
            print("sorry?")
            dancefloor2()
    
def flipcup():
    print("you're awful at this. Maybe lets try something else for a bit, im pretty sure you just drank a whole case of beer and who knows what else in one game...")     
    drunk == True
    response = raw_input("-->").lower()
    if "kitchen" in response:
        kitchen()
    elif "living room" in response:
        livingroom()
    else:
        print("sorry?")
        flipcup()
    
    
def kitchen():
    print("Oh hell yeah there's a cat in here!")
    response = raw_input("-->").lower()
    if "cat" in response or "pet" in response:
        stranger()
    elif "drink" in response:
        print("What are you drinking?")
        response = raw_input("-->").lower()
        print("good choice")
        print("there not much else going on in here. lets check out the living room or maybe play some flip cup")
        response = raw_input().lower()
        if "living room" in response:
            livingroom()
        elif "flip cup" in response or "play" in response or "dinning room" in response:
            flipcup()
    
def livingroom():
    print("the crowd seems to be dissipating and your ex just walked in the front door.")
    print("do you talk to them? or maybe it's time to call it a night?")
    response = raw_input("-->").lower()
    if "talk" in response or "ex" in response:
        ex()
    elif "leave" in response or "home" in response or "night" in response:
        home()
        
    else:
        print("sorry?")
        livingroom()
    
def stranger():
    print("the cat is walking away")
    if drunk == True:
        print("you followed the cat into someones room")
        print("")
        print("you must have been really drunk, you passed out on a strangers bed petting their cat.")
        print("sleep tight")
    elif drunk == False: 
        print("So sad :(. the cat ran away.")
        print("there not much else going on in here. lets check out the living room")
        livingroom()
                



def wreck():
    print("never drink and drive, you were involved in a head on collision on the way home and are now in the hospital in critical condition.")   

def drug():
    print("never trust a stranger.")
    print("there must have been something in that drink because all the sudden you can't walk and the next thing you know, you're in the back of an abulance on the way to the hospital.")                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
intro()
