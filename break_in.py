# adventure game

# creativity: i added a unique function i like to call the DANGER METER. it will increase or decrease depending on what the user does, and will ultimately determine whether the user wins or loses.
# also secret ending if you decide to stay in your room and go back to bed. another secret ending if you jump out the window, and another secret ending if you order pizza. i really hope that i have enough variety of scenarios, like the bedroom scenario, and then the hallway scenario, and then the living room scenario, and then the kitchen scenario, and then the final confrontation scenario. thats what you mean by scenario, right? please like an hour ago i reread the grading rubric and im afraid i misunderstood what a scenario is.
# i added branching, also i saved flashlight and managed to use it in two different areas, making it function as a tool 

print('You wake up suddenly to loud crash. You were sound asleep in the bedroom of your own home. Gradually, you come to your senses. The noise sounded like a window was broken near the living room.')
print('You have the option to DRESS YOURSELF, SEARCH the cabinets, and to PROCCEED down the hallway.')
print("NOTE: taking certain actions will increase or decrease the DANGER level. Take caution to your decisions.")
print("NOTE: answer yes or no questions with a full 'yes' or 'no', and options are displayed in full caps.")

#variables:
# LastInpoutFunction, Flashlight, 

# set the danger meter
Danger = 0

#flashlight gets mad at line 29 if i dont have this. its dumb, but true. " ' ' " IS EQUAL TO TRUE, SO I CHANGED TO FALSE. LINES 65 - 80 WORK NOW BUT ITS ONLY A TEMPORARY AND CRUDE FIX (line 26 explains the problem). WTF AM I MISSING.
FlashLight = False

# dress prompt and action.
lastInputFunction = input('\nYou notice you are wearing pajamas. would you like to get DRESSED? ')
if lastInputFunction.lower() in('dress','yourself','myself','yes','dressed'):
    print('You take the time to dress yourself in something besides your pajamas.')
    Danger = Danger + 1

# search prompt and action LINES 30-34 DONT DO ANYTHING. THEY DONT CHANGE THE FLASHLIGHT VARIABLE AT ALL. I JUST CHECKED
lastInputFunction = input('\nWould you like to SEARCH the cabinets of your room?: ')
if lastInputFunction.lower() == 'yes':
    FlashLightQuestion = input('Inside the drawer of one of your cabinets is a small flashlight. Do you TAKE it?: ')
    if FlashLightQuestion.lower() in('yes','take'):
        print('You take the flashlight.')
        FlashLight = True
    else:
        FlashLight = False
    
# prompt player to leave hallway

lastInputFunction = input('\nYou are standing in your room. would you like to LEAVE and enter the hallway?: ')
if lastInputFunction.lower() in('yes','leave'):
   print('You exit your room and enter the hallway.')
elif  lastInputFunction == input('You linger in your bedroom, and notice your bed. would you like to go back to SLEEP?: '):
    Danger = Danger + 1
    if lastInputFunction.lower() in('yes','sleep'):
        print('You climb back into bed and fall asleep. In the morning your body is found cold and dead, as the intruder has murdured you in your sleep.')
        print('YOU LOST, BIG TIME. GAME OVER')
        exit()
    else:
        print('Then you finally come to your senses and start to explore. you get a feeling that taking so long may have given the intruder a head start.')

# #this doesnt work and i dont know why. i want to allow the user to input their choices in their own order, but every attempt i've made at doing so has failed horribly. after two days of testing
# # what i have before here is the final product and i am frustrated. but this doesnt matter because the lines of code before this do work, so just ignore this angry rant and keep going.
# # lastInputFunction = input('what do ')
# # if lastInputFunction in('search'):
# #     print('you search')
# # elif lastInputFunction == 'dress':
# #     print('you dress')
# # elif lastInputFunction == 'procceed':
# #     print('you leave')

# next check the doors on rooms down the hallway, have one be locked. one use an elif to ask to open, then to turn on flashlight and look, but have nothing happen.
# have a closet you can check. inside is a baseball bat you can get to reduce danger meter

# i fixed it temporarily. these lines of code TECHNICALLY work now. :for some reason, if line 71 is false (identified by lines 27-34), line 72 still executes. why does this happen and why is it so dumb. this is the problem i've been having this whole week and the internet sucks

print('\nYou find yourself standing at the end of a dark hallway. you can CONTINUE down the hallway. throughout the hallway there are doors to other rooms of your house.')
lastInputFunction = input('What will you do? ')
if lastInputFunction.lower() in('continue','go'):
    lastInputFunction = input('\nYou walk down the dark cooridoor of your house. to your left is a door to the bathroom. The door is already ajar. \nwould you like to CHECK the door, or CONTINUE? ')
    if lastInputFunction.lower() == 'check':
        print('You gently push on the door and it swings open softly. it is too dark to see anything.')
        if FlashLight:
            lastInputFunction = input('Would you like to use your FLASHLIGHT? ')
            if lastInputFunction.lower() in('yes','flashlight'):
                print('You click on your flashlight and the bathroom is illuminated. there is nothing out of the ordinary, and nothing useful to you. You turn back to face down the hallway.')
            else:
                print('You do not use your flashlight, and hence cannot see anything, so you turn back around.')
        else:
            print('The light switch doesnt work and you do not have a way to provide light. The only option left to turn back around.')
    elif lastInputFunction.lower() == 'continue':
        print('You turn your back to the bathroom and face again down the hallway.')

# # # for some reason, even though flashlight should be false from missing line 27, it still thinks you have a flashlight on line 90. i dont know why. this was an attempt to make lines 65 - 80 work.
# # print('\nYou find yourself standing at the end of a dark hallway. you can CONTINUE down the hallway. throughout the hallway there are doors to other rooms of your house.')
# # lastInputFunction = input('What will you do? ')
# # if lastInputFunction.lower() in('continue','go'):
# #     lastInputFunction = input('You walk down the dark cooridoor of your house. To your left is a door to the bathroom. The door is already ajar. \nWould you like to CHECK the door, or CONTINUE? ')
# #     if lastInputFunction.lower() == 'check':
# #         stupidCheckWithFlashlightWorkPleaseWhyWontThisWork = True
# #     elif lastInputFunction.lower() == 'continue':
# #         print('you dont check')

# # if stupidCheckWithFlashlightWorkPleaseWhyWontThisWork and FlashLight:
# #     print('the room is dark. you use flashlight to see')
# # elif stupidCheckWithFlashlightWorkPleaseWhyWontThisWork and FlashLight == False:
# #     print('the room is dark. you have nothing to see with.')

# this is a replacement if i could not get lines 65 - 80 to work. im leaving it in because i feel like it. i dont remember why 106 - 108 was there.
lastInputFunction = input('\nyou are standing at the end of a hallway. \ndo you want to GO forward further? ')
if lastInputFunction.lower() in('go','continue'):
    print('you go down hallway')
    lastInputFunction = input('you come to a door. do you LOOK inside or NO? ')
    if lastInputFunction.lower() == 'look':
        print('you look inside. there is nothing useful here. just an empty bedroom that you have yet to make use of.')
    elif lastInputFunction.lower() == 'no':
        print('you dont look inside and keep going.')
# else:
#     print('i dont know how to repeat the line, so i guess you are screwed now')
#     exit()

print('\nYou return to the hallway. Further down is another door, this one goes to your wall closet.')
lastInputFunction = input('Would you like to SEARCH the wall closet? ')
if lastInputFunction.lower() == 'search':
    search = True
else:
    search = False

# what why if you search the wall closet, it will say you did not search the closet, but still lower the danger meter. IT NOT SUPPOSED TO DO THAT, BECAUSE THEY DIDNT FULFILL THE ELSE STATEMENT
# WHY ON EARTH IS IT DOING THIS AND HOW DO I FIX IT. THE INTERNET IS NOT HELPING. I CANT GET A TUTOR BEFORE THE DUE DATE PASSES.
if search:
    lastInputFunction = input('Inside the closet is an old baseball bat of yours. \nDo you TAKE the bat? ')
else:
    print('You chose not to search the closet and turn back to face the hallway again.')

if lastInputFunction.lower() in('yes','take'):
    Danger = Danger - 3


# enter front room and notice the broken window. if you search the room you will step on the glass, alerting the intruder and increasing the danger meter. added branching options in case scenarios on the rubric wanted branching

print('\nYour investigation leads you to the front room. a brisk breeze can be felt, and the source becomes obvious when you notice the broken window.')
lastInputFunction = input('Would you like to INVESTIGATE further, JUMP out the window, or CONTINUE? ')
if lastInputFunction.lower() in('yes','search','investigate'):
    print('You walk closer to the window to get more information, but clumsily step on the broken glass. it cracks noisily, and you suddenly hear shuffling from your kitchen. \nThe intruder knows you are there.')
    Danger = Danger + 1
elif lastInputFunction.lower() == 'jump':
    print('you jump out the window and are presented with two options')
    lastInputFunction = input('you can run to the POLICE station, or you can run to the NEIGHBORS house. ')
    if lastInputFunction.lower() == 'police':
        print('you arrive at the station. you run up to the office at the counter, and he asks you what you need')
        lastInputFunction = input('you can TAKE his gun, or you can file a REPORT. ')
        if lastInputFunction.lower() == 'take':
            print('you ask for the officers gun, stating its an emergency. when you are refused, you try to take it from him. as a result, you are placed under arrest')
            print('BRANCH ENDING: IDIOT')
            exit()
        elif lastInputFunction.lower() == 'report':
            print('you file a report, and a few days later the criminal is caught')
            print('BRANCH ENDING: SMART')
            exit()
    elif lastInputFunction.lower() == 'neighbors':
        print('you run up to the neighbors door, knocking on their front door frantically. the owner opens the door with groggy confusion')
        lastInputFunction = input('ask for HELP, or take REFUGE')
        if lastInputFunction.lower() == 'help':
            print('the neighbor obliges, grabs their shotgun, and together you defeat the intruder')
            print('BRANCH ENDING: BATTLE BROTHERS')
            exit()
        elif lastInputFunction.lower == 'refuge':
            print('you crash on their couch for the night. you are safe, but when you return to you own home the next day all of you most valuable belongings have been burgled.')
            print('BRANCH ENDING: DESTITUTE')
            exit()
else:
    print('you choose not to look at the front room.')

# move to the kitchen. if you search the kitchen you can identify that the knives are missing. if you dont search the danger meter increases.

print('\nSkillfully, you make your way into the kitchen. there is no obvious danger, so you may SEARCH more closely if you wish.')
lastInputFunction = input('Do you want to search the kitchen? ')
if lastInputFunction.lower() in('yes','search','investigate','identify','anything else'):
    print('Your attention is drawn to the kitchen knife holder, which stands empty. The intruder may be armed, but now you are prepared for it')
    Danger = Danger + 1
else:
    Danger = Danger + 2


# move into the dining room and notice a landline phone on the wall. prompt to call someone. if the police is called, the danger meter will be reduced. easter egg if you call for pizza.

print('\nNext you slink into the dining room. on the wall you notice your landline, wall-mounted, battery-powered, still working home phone. you could dial up a number if you wish. ')
phoneCall = input('what number would you like to call? ')
if phoneCall.lower() in('911','police','authorities'):
    print('You dial in the number and let it rign out. The police should arrive to check it out. Help is on the way')
    Danger = Danger -1
elif phoneCall.lower() in('pizza','little','ceasars','dominos',"domino's",'door','dash'):
    print('The phone rings for a moment before the pizza delivery service responds. You start to order your favorite pizza, when from around the corner the intruder intrudes, asking for a large pepperoni and sausage.')
    print('Once the order is confirmed and paid for, the food is delivered and you and your new indrusive friend spend the rest of the night laughing, talking, and playing games.')
    print('SECRET ENDING UNLOCKED. PIZZA POWER!')
    exit()
else:
    print('the number you call starts to ring, but before anyone answers...')

# at the end of another hallway you will see a figure. if have flashlight, prompt to shine light to reduce danger level. if police called, detail police sirens being audible
# give options for how to engage the threat; aggressive to increase danger, defensive to decrease danger. measure the danger meter, determine if user is successful or fails.

print('\nSuddenly, the sillohouette separates itself from the shadows of a hallway and approaches you. the intruder stands before you, and confrontation in inevitable.')
lastInputFunction = input("The intruder approaches threateningly. You have to make you move. do you take an AGGRESSIVE action, and charge your foe, or do you take a DEFENSIVE action, and prepare to weather the intruder's assault")
if lastInputFunction.lower() == 'defensive':
    print('You brace yourself and look for a chance to disarm the intruder!')
    Danger = Danger - 1
elif lastInputFunction.lower() == 'aggressive':
    print('You act on instinct, lunging for a first strike against the intruder!')
    Danger = Danger + 1
else:
    print('That action is not supported in this fight. your unpreparedness is your own undoing')
    Danger = Danger + 3

# moment of truth. hold fast, or perish
if phoneCall.lower() in('911','police','authorities'):
    print('The harsh flashing lights of the police illuminate your household.')
if Danger >= 0:
    print('Unfortunately, the intruder had gotten the better of you. It was brave holding your own against them, but really you never stood a chance. maybe next time you will fare better.')
    print('GAME OVER: LOSS')
    exit()
else:
    print('Triumphantly, you stand over your would-be killer. The intruder was successfully apprehended by your efforts, and you are named a hero in the news that very morning.')
    print('GAME OVER: OVERWHELMING VICTORY!')

print(Danger)
