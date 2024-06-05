has_axe = False
has_boltcutters = False
smashed_mirror = False
has_key = False
rotting_food = False
old_man = False
has_soup = False
seen_soup = False
talked = False
named = False
opened_fridge = False
read_terminal = False
has_tuna = False
fridge_again = False
has_orange_cat = False
has_grey_cat = False
seen_cat = False
broken_chair = False

def awake():
    print("You wake up, becoming conscious for the first time in what feels like forever.")
    bedroom()
    
def bedroom():
    global read_terminal
    if read_terminal == True:
        print("You are in a simple bedroom, but something feels... off. There is a window that has been completely boarded up. There is a door on one side of the room and a sheet of paper hung up in the corner.")
        print("You feel as though you are being watched. The only place anything could hide would be... underneath the bed. Very original.")
        response = raw_input("> ").lower()
        if "door" in response or "living room" in response: 
            living_room()
        elif "paper" in response or "note" in response:
            print("Whatever was previously written on the paper has been agressively scratched out. Instead, in horrid handwriting, the paper now states: 'YOU CAN'T LEAVE ME HERE'")
            bedroom()
        elif "window" in response:
            print("The window is completely boarded up. It's probably best to leave it that way.")
            bedroom()
        elif "bed" in response or "underneath" in response:
            print("You check under the bed. There is a humanoid figure ridiculously contorted in order to fit underneath. As soon as your eyes meet its deformed face, you notice that one of its hands is covering its eyes, preventing you from looking into them. The other hand is reaching out, pointing towards the paper in the corner of the room.")
            bedroom()
        else:
            print("You cannot do that at the moment.")
            bedroom()
    if read_terminal == False:
        print("You are in a simple bedroom, but something feels... off. There is a window that has been completely boarded up. There is a door on one side of the room and a sheet of paper hung up in the corner.")
        print("What do you want to do?")
        response = raw_input("> ").lower()
        if "door" in response or "living room" in response: 
            living_room()
        elif "paper" in response:
            print("The paper is a hastily written note that seems to be written in your handwriting. It reads: 'DON'T LOOK OUTSIDE'")
            bedroom()
        elif "window" in response:
            print("The window is completely boarded up. It's probably best to leave it that way.")
            bedroom()
        else:
            print("You cannot do that at the moment.")
            bedroom()
            
def living_room():
    global has_axe
    global smashed_mirror
    global broken_chair
    if smashed_mirror == False and broken_chair == False:
        print("You are in the living room. There is a large mirror fixed into the wall and an old-looking fancy armchair. There is a passage into the kitchen and a door leading back to the bedroom. You feel as though you are being watched.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if ("mirror" in response) and has_axe == False:
            print("As you gaze into the mirror, the feeling of being watched grows stronger. The glass is too thick to break with your bear hands.")
            living_room()
        elif ("break mirror" in response or "smash mirror" in response or "shatter mirror" in response) and has_axe == False:
            print("The glass is too thick to break with your bare hands.")
            living_room()
        elif "chair" in response or "sit" in response:
            print("You go over and sit in the old armchair, which gives a loud creak as you sit down.")
            chair()
        elif "door" in response or "bedroom" in response:
            bedroom()
        elif ("break mirror" in response or "shatter mirror" in response or "use axe" in response or "smash mirror" in response) and has_axe == True:
            print("You shatter the glass and see two beady eyes staring at you. You freeze in fear.")
            smashed_mirror = True
            awake()
        elif "kitchen" in response or "passage" in response:
            kitchen()
        else:
            print("You cannot do that at the moment.") 
            living_room()
    if smashed_mirror == False and broken_chair == True:
        print("You are in the living room. There is a large mirror fixed into the wall and a broken old-looking armchair. There is a passage into the kitchen and a door leading back to the bedroom. You feel as though you are being watched.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if ("mirror" in response) and has_axe == False:
            print("As you gaze into the mirror, the feeling of being watched grows stronger. The glass is too thick to break with your bear hands.")
            living_room()
        elif ("break mirror" in response or "smash mirror" in response or "shatter mirror" in response) and has_axe == False:
            print("The glass is too thick to break with your bare hands.")
            living_room()
        elif "chair" in response or "sit" in response:
            print("You gaze upon the wreckage of the formerly functional armchair and a sense of hopelessness washes over you.")
            living_room()
        elif "door" in response or "bedroom" in response:
            bedroom()
        elif ("break mirror" in response or "shatter mirror" in response or "use axe" in response or "smash mirror" in response) and has_axe == True:
            print("You shatter the glass and see two beady eyes staring at you. You freeze in fear.")
            smashed_mirror = True
            awake()
        elif "kitchen" in response or "passage" in response:
            kitchen()
        else:
            print("You cannot do that at the moment.") 
            living_room()
    if smashed_mirror == True and broken_chair == True:
        print("You are in the living room. There is a passage to the kitchen and a door to the bedroom. There is a broken old-looking armchair. There is also a large mirror that has been shattered, revealing a hidden labratory.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "labratory" in response or "lab" in response:
            labratory()
        elif "chair" in response:
            print("You gaze upon the wreckage of the armchair and mourn its former beauty.")
            living_room()
        elif "kitchen" in response or "passage" in response:
            kitchen()
        elif "bedroom" in response or "door" in response:
            bedroom()
        else:
            print("You cannot do that at the moment.") 
            living_room()
    if smashed_mirror == True and broken_chair == False:
        print("You are in the living room. There is a passage to the kitchen and a door to the bedroom. There is an old-looking fancy armchair. There is also a large mirror that has been shattered, revealing a hidden labratory.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "labratory" in response or "lab" in response:
            labratory()
        elif "kitchen" in response or "passage" in response:
            kitchen()
        elif "bedroom" in response or "door" in response:
            bedroom()
        elif "chair" in response or "sit" in response:
            print("You go over to the chair and begin to sit down.")
            chair()
        else:
            print("You cannot do that at the moment.") 
            living_room()
def chair():
    global broken_chair
    print("The armchair doesn't seem very stable, but you are very comfortable. There is a handle on the side of the chair that you can pull.")
    print("What would you like to do?")
    response = raw_input("> ").lower()
    if "pull" in response or "handle" in response:
        print("You pull on the handle and the chair jerks back, startling you. A footrest protrudes from the bottom of the chair. You begin to feel somewhat sleepy. What would you like to do?")
        response = raw_input("> ").lower()
        if "footrest" in response or "sleep" in response:
            print("You place your feet on the footrest and stretch out while yawning. You begin to doze off.")
            print("You dream of unsettling beady eyes leering down at you as spindly, cold fingers begin to wrap around you.")
            awake()
        elif "under" in response:
            print("You check under the footrest but do not see anything other than dust. Suddenly, the chair begins to creak louder until eventually the bottom falls out and the whole chair collapses. You hear a low chuckle coming from the mirror.")
            broken_chair = True
            living_room()
        else:
            print("You cannot do that at the moment. You keep sitting on the chair, beginning to doze off, until the bottom of the chair gives out and the whole thing collapses. You hear a quiet low chuckle coming from the mirror.")
            broken_chair = True
            living_room()
            
def kitchen():
    global rotting_food 
    global has_boltcutters
    print("You are in the kitchen. There is an uncovered window. You feel an unreasonable urge to look through the window. There are some cabinets and a strangely tall table with rotting food on top of it. There is a door to the garage and a passageway leading to the living room.")
    print("What would you like to do?")
    response = raw_input("> ").lower()
    if "window" in response:
        print("You catch a glimpse of what is outside the window and freeze in fear. You feel an immense pressure building behind your eyes until you eventually pass out.")
        awake()
    elif "cabinet" in response:
        cabinet()
    elif "rotting food" in response or "rotten food" in response:
        print("What would you like to do with the rotting food?")
        response = raw_input("> ").lower()
        if ("grab" in response or "take" in response) and rotting_food == False:
            print("Your nose scrunches up as you grab a handfull of rotting food. You now have rotting food. Congratulations.")
            rotting_food = True
            kitchen()
        elif ("take" in response or "grab" in response) and rotting_food == True:
            print("You grab even more rotting food. You'd think one handfull would be enough...")
            kitchen()
        elif "eat rotting food" in response or "eat food" in response or "eat" in response:
            print("You hesitantly bring the rotting food to your mouth and take a bite. You are immediately filled with regret as you begin retching.")
            kitchen()
        else:
            print("You cannot do that at the moment.")
            kitchen()
    elif ("underneath table" in response or "under table" in response) and has_boltcutters == False:
        print("You look underneath the table and see a pair of bolt cutters taped to the underside of the table. I wonder why anyone would put them there...")
        print("What would you like to do with the boltcutters?")
        response = raw_input("> ").lower()
        if "take" in response or "grab" in response:
            print("You take the boltcutters.")
            has_boltcutters = True
            kitchen()
        elif "leave" in response:
            print("You leave the boltcutters where they are.")
            kitchen()
        else:
            print("You cannot do that right now.")
            kitchen()
    elif ("underneath table" in response or "under table" in response) and has_boltcutters == True:
        print("There is nothing else under the table.")
        kitchen()
    elif "garage" in response or "door" in response:
        garage()
    elif "living room" in response or "passageway" in response:
        living_room()
    else:
        print("You cannot do that at the moment.")
        kitchen()
        
def cabinet():
    global has_soup
    global seen_soup
    if has_soup == False and seen_soup == False:
        print("You look in the cabinet and see a can of soup. What would you like to do?")
        response = raw_input("> ").lower()
        if "take" in response:
            print("You take the can of soup.")
            has_soup = True
            seen_soup = True
            kitchen()
        elif "eat" in response:
            print("You eat the soup, no hesitation. Who knows if it could've been used elsewhere...")
            seen_soup = True
            has_soup = False
            kitchen()
        elif "leave" in response:
            print("You leave the can of soup in the cabinet.")
            kitchen()
        else:
            print("You cannot do that at the moment.")
            cabinet()
    if seen_soup == True:
        print("You check in the cabinet again and see that it is empty.")
        kitchen()
def garage():
    global has_axe
    global name
    global old_man
    global talked
    if talked == False:
        print("You are in the garage. There is a tool closet and a large painting hanging on the wall. There is a skeletal old man in the corner motioning at you you come closer. There is a door leading to the kitchen.")
        response = raw_input("> ").lower()
        if "door" in response or "kitchen" in response:
            kitchen()
        elif ("tool closet" in response or "closet" in response) and has_boltcutters == False:
            print("The tool closet is bolted shut. You would need boltcutters to open it.")
            garage()
        elif ("tool closet" in response or "closet" in response) and has_boltcutters == True:
            tool_closet()
        elif ("painting" in response or "view painting" in response):
            print("You look at the painting, which depicts a grey cat sitting atop a cat tower. There is a plaque underneath it that says, 'Balloo' . The painting is too heavy for you to move.")
            garage()
        elif("cut painting" in response or "axe painting" in response or "stab painting" in response) and has_axe == True:
            print("The painting is so beautiful, you really don't want to damage it.")
            garage()
        elif "old man" in response or "man" in response or "talk" in response:
            old_man()
        else:
            print("You cannot do that at the moment.")
            garage()
    if talked == True:
        print("You are in the garage. There is a tool closet and a large painting hanging on the wall. The skeletal old man is still in the corner. There is a door leading to the kitchen.")
        response = raw_input("> ").lower()
        if "door" in response or "kitchen" in response:
            kitchen()
        elif ("tool closet" in response or "closet" in response) and has_boltcutters == False:
            print("The tool closet is bolted shut. You cannot open it right now.")
            garage()
        elif ("tool closet" in response or "closet" in response) and has_boltcutters == True:
            tool_closet()
        elif("cut painting" in response or "axe painting" in response or "stab painting" in response) and has_axe == True:
            print("The painting is so beautiful, you really don't want to damage it.")
            garage()
        elif ("painting" in response or "view painting" in response):
            print("You look at the painting, which depicts a grey cat sitting atop a cat tower. There is a plaque underneath it that says, 'Balloo' . The painting is too heavy for you to move.")
            garage()
        elif "old man" in response or "man" in response or "talk" in response:
            old_man()
        else:
            print("You cannot do that at the moment.")
            garage()
def tool_closet():
    global has_axe
    if has_axe == False:
        print("You use the boltcutters to open the tool closet and see an axe. What would you like to do with it?")
        response = raw_input("> ").lower()
        if "take" in response or "grab" in response:
            print("You take the axe.")
            has_axe = True
            garage()
        elif "leave" in response:
            print("You leave the axe.")
            garage()
        else:
            print("You cannot do that right now.")
            tool_closet()
    if has_axe == True:
        print("The tool closet is empty.")
        garage()    
        
def old_man():
    global talked
    global name
    global named
    if talked == False:
        print("The old man motions for you to come closer and you do. His voice is a hoarse whisper.")
        if named == False:
            print("OLD MAN > 'what is your name?'")
            name = raw_input("> ")
            named = True
            print("OLD MAN > '" + name + ", huh? That's... an interesting name. Have you ever thought of changing it?")
            response = raw_input("> ").lower()
            if "yes" in response or "yeah" in response:
                print("OLD MAN > 'Just didn't carry through with it huh? I see how it is.'")
                favor()
            elif "no" in response or "nope" in response:
                print("OLD MAN > 'You might want to.'")
                favor()
            else:
                print("OLD MAN > 'Whatever.'")
                favor()
        if named == True:
            print("OLD MAN > 'Truly such as shame about your name, " + name + ".'")
            favor()
    elif talked == True:
        print("The old man appears to be asleep, but he might just be faking it. Either way, he doesn't seem to want to talk to you right now.")
        garage()
        
def favor():
    global talked
    global name
    global has_key
    print("OLD MAN > 'Anyway, could I ask you a favor?'")
    response = raw_input("> ").lower()
    if "yes" in response or "sure" in response or "what" in response or "ok" in response:
        print("OLD MAN > 'Please feed me, " + name + ". I am so, so hungry. They do not feed me anymore.'")
        response = raw_input("> ").lower()
        if ("soup" in response or "can" in response) and has_soup == True:
            print("You give the old man the can of soup. He looks very pleased with your food offering and eats it at an impressive speed. You feel as though you can physically see him regain much of his strength.")
            print("OLD MAN > 'That was the best thing I have eaten in my entire life. Thank you! Here, let me show you something.'")
            print("The old man gets up and walks over to the painting. He grabs it off of the wall and you see a tiny silver key fall from behind it. He picks up the key and hands it to you. He then places the painting back on the wall.")
            has_key = True
            talked = True
            garage()
        elif ("soup" in response or "can" in response) and has_soup == False:
            print("You do not have that. The old man seems to be growing impatient.")
            garage()
        elif ("rotten food" in response or "rotting food" in response or "food" in response) and rotting_food == True:
            print("You give the old man a handful of the rotting food from earlier. He lets out a shaky sigh and begins eating.")
            print("OLD MAN > 'That was horrible, but thanks, I guess. I'm still hungry though. Could you come a little closer? I just want to see something.'")
            response = raw_input("> ").lower()
            if "no" in response or "nope" in response or "run" in response:
                print("The old man begins laughing.")
                print("OLD MAN > 'Whatever, just get out of my face.'")
                talked = True
                garage()
            elif "ok" in response or "yes" in response or "closer" in response:
                print("You gradually come closer to the old man. You watch as his jaw unhinges and his mouth slowly extends towards you. The last thing you experienced was his foul smelling breath.")
                exit()
            else:
                print("The old man looks confused. You watch as his jaw unhinges and his mouth slowly extends towards you. The last thing you experienced was his foul smelling breath.")
                exit()
        elif ("rotten food" in response or "rotting food" in response) and rotting_food == False:
            print("You don't have that right now. The old man seems to be growing impatient.")
            garage()
        elif "no" in response or "nah" in response or "nope" in response:
            print("The old man rolls his eyes. He then begins laughing.")
            print("OLD MAN > 'If you won't feed me, I'll just help myself.'")
            print("You watch, horrified, as the old man's jaws become unhinged. His mouth slowly extends towards you. The last thing you experienced was his foul smelling breath.")
            exit()
        else:
            print("The old man doesn't understand your answer.")
            garage()
            
    elif "no" in response or "nope" in response or "not" in response:
        print("OLD MAN > 'Whatever, your loss'")
        garage()
    else:
        print("OLD MAN > 'I'm afraid I don't understand what you're saying.'")
        favor()

def labratory():
    global has_key
    global has_grey_cat
    global has_orange_cat
    print("You are in the labratory. There is a locked box on one of the shelves and a stairway leading downstairs. There is also a passage to the living room.")
    if has_grey_cat == True:
        print("The grey cat currently following you begins to walk over to a small hatch that you did not notice before. The cat stops in front of the hatch and stares at you while repeatedly meowing.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "open" in response:
            print("You open the hatch and are blinded by sunlight. You smell fresh air for what seems like the first time. You step outside and the cat follows you. You do not remember anything about yourself other than your name, " + name + ". But you feel as though you can start anew.")
            print("You are free, exclusing the PTSD that will likely haunt you for the rest of your life. But hey you can always try getting that treated, hopefully.")
            exit() 
        elif "cat" in response:
            print("You look down at the cat, that is still incessantly meowing at you. It seems to be urging you to make a descision.")
            labratory()
        elif "leave" in response or "ignore" in response:
            print("You ignore the cat. You turn away from it and when you look at it again, it is gone.")
            has_grey_cat = False
            labratory()
        else:
            print("You cannot do that at the moment.")
            labratory()
    if has_orange_cat == True:
        print("The orange cat currently following you begins to walk over to a dark corner of the lab where you see it staring at some closed blinds you never noticed before. It begins clawing at the blinds.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "blinds" in response or "open" in response:
            print("You slowly begin to open the blinds. As soon as you catch a glimpse of what is behind them, you freeze in fear. The cat jumps on you and begins clawing at your spine. The burning pain soon fades into nothing.")
            exit() 
        elif "cat" in response:
            print("You look down at the cat that is staring eerily at you. It seems to be urging you to make a certain descision.")
            labratory()
        elif "leave" in response or "ignore" in response:
            print("You ignore the cat. You turn away from it and when you look at it again, it is gone.")
            has_orange_cat = False
            labratory()
        else:
            print("You cannot do that at the moment.")
            labratory()
    if has_orange_cat == False or has_grey_cat == False:
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "box" in response and has_key == False:
            print("You need a key to open the locked box.")
            labratory()
        if ("key" in response or "open" in response) and has_key == True:
            print("You use the key from the old man to open the locked box and you find a bloody letter inside. It reads:")
            print("'To Steve: you are a sick, sick individual. I understand the need to research the unknown, but leave innocent humans out of it. I quit.'")
            labratory()
        elif "stairway" in response or "downstairs" in response or "stairs" in response or "down" in response: 
            basement()
        elif "living room" in response:
            living_room()
        else:
            print("You cannot do that at the moment.")
            labratory()
    
def basement():
    global opened_fridge
    global read_terminal
    global has_tuna
    global fridge_again
    global has_grey_cat
    global has_orange_cat
    global seen_cat
    if has_tuna == True and seen_cat == False:
        print("You are in the basement. It is very dark and you feel quite uneasy. There is a desk with an old computer resting on it and a rusty, gross looking fridge on one side of the room. There is a stairway leading back upstairs.")
        print("You feel something brush up against your leg and look down to see a grey cat and an orange tabby.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "cats" in response or "cat" in response:
            print("You crouch down to the cats and see them sniffing where you are keeping the tuna. What would you like to do?")
            response = raw_input("> ").lower()
            if "eat tuna" in response:
                print("You eat the tuna in front of the cats. They look shocked. After a second, the orange one leaps at you and scratches your eyeballs. You try to shove it off of you but it is ridiculously persistent. The cat claws through your eye sockets and into your brain, leaving you dead.")
                exit()
            elif ("give" in response or "feed" in response) and ("orange" in response or "tabby" in response):
                print("You give the tuna to the orange cat and it happily eats the whole container while purring. It now follows you.")
                has_cat = True
                seen_cat = True
                has_tuna = False
                basement()
            elif ("give" in response or "feed" in response) and ("grey" in response or "gray" in response):
                print("You give the tuna to the grey cat and it happily eats the whole container while purring. It now follows you.")
                has_grey_cat = True
                seen_cat = True
                has_tuna = False
                basement()
            elif "nothing" in response:
                print("You do nothing and the cats eventually fade into the labratory, where you presume they somehow came from.")
                seen_cat = True
                basement()
            elif "give" in response or "feed" in response:
                print("Which cat would you like to give it to?")
                response = raw_input("> ").lower()
                if "orange" in response or "tabby" in response:
                    print("You give the tuna to the orange cat and it happily eats the whole container while purring. It now follows you.")
                    has_orange_cat = True
                    has_tuna = False
                    seen_cat = True
                    basement()
                elif "grey" in response or "gray" in response:
                    print("You give the tuna to the grey cat and it happily eats the whole container while purring. It now follows you.")
                    has_grey_cat = True
                    seen_cat = True
                    has_tuna = False
                    basement()
                else:
                    print("You cannot do that at the moment.")
                    basement()
            else:
                print("You cannot do that at the moment.")
                basement()
        elif "computer" in response:
            print("You press a button on the computer and the screen appears to show some kind of terminal interface. It is asking for a password. What will you type?")
            response = raw_input("> ").lower()
            if "balloo" in response:
                print("You type in '" + response + "' into the terminal and the computer begins processing something for a second. The password seems to have been correct.")
                terminal()
            else:
                print("You type in '" + response + "' in the terminal. The computer processes something for a second and the words 'INCORRECT PASSWORD' blink back at you from the screen.")
                basement()
        elif "upstairs" in response or "stairs" in response or "back" in response or "stairway" in response:
            labratory()
        elif "desk" in response:
            print("You inspect the desk and see a photograph of a sleeping grey cat. Very cute. You flip the photograph over and see a word scribbled in pencil beginning with 'Bal' that has been worn over time. I wonder what it originally said... ")
            basement()
        elif "fridge" in response:
            fridge()
        else:
            print("You cannot do that at the moment.")
            basement()
    if has_tuna == False or seen_cat == True:
        print("You are in the basement. It is very dark and you feel quite uneasy. There is a desk with an old computer resting on it and a rusty, gross looking fridge on one side of the room. There is a stairway leading back upstairs.")
        print("What would you like to do?")
        response = raw_input("> ").lower()
        if "computer" in response:
            print("You press a button on the computer and the screen appears to show some kind of terminal interface. It is asking for a password. What will you type?")
            response = raw_input("> ").lower()
            if "balloo" in response:
                print("You type in '" + response + "' into the terminal and the computer begins processing something for a second. The password seems to have been correct.")
                terminal()
            else:
                print("You type in '" + response + "' in the terminal. The computer processes something for a second and the words 'INCORRECT PASSWORD' blink back at you from the screen.")
                basement()
        elif "upstairs" in response or "stairs" in response or "back" in response or "stairway" in response:
            labratory()
        elif "desk" in response:
            print("You inspect the desk and see a photograph of a sleeping grey cat. Very cute. You flip the photograph over and see a word scribbled in pencil beginning with 'Bal' that has been worn over time. I wonder what it originally said... ")
            basement()
        elif "fridge" in response:
            fridge()
        else:
            print("You cannot do that at the moment.")
            basement()
    
        
def terminal():
    global name
    global read_terminal
    print("The screen displays the following:")
    print("> FILE 1: unit 067")
    print("> FILE 2: unit 336")
    print("> FILE 3: unit [REDACTED]")
    print("> FILE 4: CONTAINMENT BREACH - FACULTY WIDE NOTICE OF EVACUATION")
    print("> FILE 5: Human Specimen List")
    print("> OPTION 6: Exit annoyingly text-heavy terminal")
    print("Select the file you wish to view.")
    response = raw_input("> ").lower()
    if "1" in response or "067" in response:
        print("> DATA ENTRY 11/17 at 7:31 by Steve - Unit 067")
        print("Unit 067 remains largely unapproachable. Do not initiate eye contact, or Unit 067 will react negatively. Despite this hostility, Unit 067 still shows a strange amount of care for harmed or incapacitated human specimens. Similar to Unit [REDACTED] , Unit 067 typically induces some amount retrograde amnesia within the victim upon sight. Unit 067 has a highly inquisitive nature and enjoys 'stalking' . Unit 067 can contort its body inconceivably well, allowing it to get into ideal 'stalking' locations.")
        print("Note - Every attempt to prevent Unit 067 from somehow entering the labratory has been futile. Before leaving the home, check that Unit 067 has not snuck into fridge again. I need to keep Unit 336 fed.")
        terminal()
    if "2" in response or "336" in response:
        print("> DATA ENTRY 10/07 at 12:29 by Steve - Unit 336")
        print("Unit 336 takes the form of an old man. PLEASE remember to feed Unit 336 sufficiently and on time, as it has inconvinient tendencies of attempting to eat those who insufficiently feed it. Don't let any human specimens in the garage, or else Unit 336 will try to get them to feed it.") 
        terminal()
    if "3" in response or "redacted" in response:
        print("> DATA ENTRY 12/10 at 3:49 by Steve - Unit [REDACTED]")
        print("Unit [REDACTED] is extremely dangerous. Any human that sees Unit [REDACTED] will experience sharp, shooting pain along the optic nerve and will cause nearly detrimental retrograde amnesia in the victim. Despite the updated homely environment, Unit [REDACTED] hates its captivity and desperately tries to escape.")
        terminal()
    if "4" in response or "evacuation" in response or "containment breech" in response or "notice" in response:
        print("> NOTICE - CONTAINMENT BREECH")
        print("There has been a containment breech and Unit [REDACTED] has escaped containment. It cannot get past the outer walls of the facility into civilization, but all staff must evacuate the premises.")
        print("UPDATE: All staff have safely vacated the premises, and it has been deemed too dangerous to re-enter until further notice. Thank you for working with us.")
        terminal()
    if "5" in response or "Specimen" in response or "list" in response:
        print("> DATA ENTRY 12/30 at 1:41 by Steve - Human Specimen List")
        print("Due to the recent accident I regret to say that I have lost my job at the facility. They're making me publish a list of the human specimens who have 'non-consensually' aided in my research. Clearly they want to make an example out of me and act as though they had no clue what was going on down here.")
        print("I sent them the list of specimens, but really, I haven't used many. Only 13 of them. I did have to tell them about Specimen 13 (formerly known as '" + name + "') , and how they're still in that godforsaken facility. I bet they're scared shitless, they had a very anxious demeanor even before we exposed them to any units.")
        print("There's really no way out for Specimen 13. And Unit [REDACTED] probably won't enter the house ever again after escaping, so it'll just be stuck in the courtyard. Oh well, not my job to care anymore, I guess.")
        terminal()
    if "exit" in response or "6" in response:
        read_terminal = True
        basement()
    else:
        print("The terminal did not understand your input.")
        terminal()

       
def fridge():
    global has_tuna
    global opened_fridge
    global fridge_again
    if fridge_again == True:
        print("You get closer to the fridge but the smell is so horrid you just cannot take it anymore. You refuse to come any closer to the fridge.")
        basement()
    if opened_fridge == False:
        print("As you get nearer to the fridge, a foul odor grows stronger. Eventually you find yourself standing directly in front of it. You think you can hear some harsh breathing through the fridge door. What would you like to do?")
        response = raw_input("> ").lower()
        if "open" in response:
            print("You grab the handle and begin pulling the fridge door open. The foul odor grows overwhelmingly strong and you avert your head instinctually away from the source. After a second or two, you look back to the fridge. Two familiar beady eyes catch yours and you freeze in fear.")
            opened_fridge = True
            awake()
        elif "knock" in response:
            print("You knock on the fridge door. You hear a hitch in the breathing behind the door. Slowly, the fridge door creaks open seemingly on its own until you see a lanky hand pushing it open from the inside. Two beady eyes meet yours. You freeze in fear.")
            opened_fridge = True
            awake()
        else:
            print("You cannot do that at the moment.")
            fridge()
    if opened_fridge == True:
        print("You glance at the foul-smelling fridge and begin to hesitantly advance towards it. Soon you are standing directly in front of it. The door is closed. What would you like to do?")
        response = raw_input("> ").lower()
        if "open" in response:
            print("Bracing yourself for the foul smell, you open the fridge to see a significant amount of rotting food and some other ominous rotting substances. You also see a can of tuna that looks comparitively delicious.")
            print("What would you like to do?")
            response = raw_input("> ").lower()
            if "eat tuna" in response:
                print("You eat the tuna. Delicious! Now your breath smells bad, though.")
                fridge_again = True
                basement()
            elif "take tuna" in response:
                print("You take the tuna.")
                has_tuna = True
                fridge_again = True
                basement()
            elif "take rotten" in response or "take rotting" in response:
                print("You take the rotten substance. What a nice thing to have.")
                fridge_again = True
                basement()
            elif "eat rotten" in response or "take rotting" in response:
                print("You eat a handful of the rotten substance. You immediately regret it and question why you act the way you act sometimes.")
                fridge_again = True
                basement()
            elif "leave" in response or "exit" in response or "nothing" in response:
                fridge_again = True
                basement()
            else:
                print("You cannot do that right now.")
                basement()
        else:
            print("You cannot do that at the moment.")
            basement()

awake()
