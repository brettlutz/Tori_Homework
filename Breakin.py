##Okay dad, I tried to make this all as nested as possible, i didn't want to reorganize too much especially since
#everything is a mess before I even touch anything


# set the danger meter
Danger = 0

def hallway ():
    Hall = input('\nYou are standing in your room. would you like to LEAVE and enter the hallway or STAY?: ')
    if Hall.lower() == 'leave':
     print('You exit your room and enter the hallway.')
     hall_cont()
    elif  Hall == 'STAY':
      bed = input('You linger in your bedroom, and notice your bed. would you like to go back to SLEEP?: ')
      Danger = Danger + 1
      if bed.lower() == 'SLEEP':
        print('You climb back into bed and fall asleep. In the morning your body is found cold and dead, as the intruder has murdered you in your sleep.')
        print('YOU LOST, BIG TIME. GAME OVER')
        exit()
      else:
        print('Then you finally come to your senses and start to explore. you get a feeling that taking so long may have given the intruder a head start.')
        Danger += 5
        hall_cont()
        
def hall_cont():       
    print('\nYou find yourself standing at the end of a dark hallway. you can CONTINUE down the hallway. throughout the hallway there are doors to other rooms of your house.')
    lastInputFunction = input('What will you do? ')
    if lastInputFunction.lower() in('continue','go'):
        lastInputFunction = input('\nYou walk down the dark corridor of your house. to your left is a door to the bathroom. The door is already ajar. \nwould you like to CHECK the door, or CONTINUE? ')
        if lastInputFunction.lower() == 'check':
            print('You gently push on the door and it swings open softly. it is too dark to see anything.')
            Danger = Danger + 1
            leave_hall()
            if FlashLight:
                lastInputFunction = input('Would you like to use your FLASHLIGHT? ')
                if lastInputFunction.lower() in('yes','flashlight'):
                  Danger = Danger + 1  
                  print('You click on your flashlight and the bathroom is illuminated. there is nothing out of the ordinary, and nothing useful to you. You turn back to face down the hallway.')
                  leave_hall()
                else:
                    print('You do not use your flashlight, and hence cannot see anything, so you turn back around.')
                    Danger = Danger + 1
                    leave_hall()
            else:
                Danger = Danger + 1
                print('The light switch doesn\'t work and you do not have a way to provide light. The only option left to turn back around.')
                leave_hall()
        elif lastInputFunction.lower() == 'continue':
            print('You turn your back to the bathroom and face again down the hallway.')
            leave_hall()
            
def leave_hall ():
    lastInputFunction = input('\nyou are standing at the end of a hallway. \ndo you want to GO forward further? ')
    if lastInputFunction.lower() in('go','continue'):
      print('you go down hallway')
      lastInputFunction = input('you come to a door. do you LOOK inside or NO? ')
      if lastInputFunction.lower() == 'look':
          print('you look inside. there is nothing useful here. just an empty bedroom that you have yet to make use of.')
          too_many_hall_prompts()
      elif lastInputFunction.lower() == 'no':
          print('you dont look inside and keep going.')
          too_many_hall_prompts()
  
def too_many_hall_prompts():      
  lastInputFunction = input('\nyou are standing at the end of a hallway. \ndo you want to GO forward further? ')
  if lastInputFunction.lower() in('go','continue'):
    print('you go down hallway')
    lastInputFunction = input('you come to a door. do you LOOK inside or NO? ')
    if lastInputFunction.lower() == 'look':
        print('you look inside. there is nothing useful here. just an empty bedroom that you have yet to make use of.')
        print('\nYou return to the hallway. Further down is another door, this one goes to your wall closet.')
        lastInputFunction = input('Would you like to SEARCH the wall closet? ')
        if lastInputFunction.lower() == 'search':
         search = True
         if search:
          lastInputFunction = input('Inside the closet is an old baseball bat of yours. \nDo you TAKE the bat? ')
          if lastInputFunction.lower() in('yes','take'):
           Danger = Danger - 3
           rooms()
        else:
          print('You chose not to search the closet and turn back to face the hallway again.')
          rooms()

    else:
         search = False
         print('you dont look inside and keep going.')
         rooms()
         
def rooms():
    print('\nYour investigation leads you to the front room. a brisk breeze can be felt, and the source becomes obvious when you notice the broken window.')
    lastInputFunction = input('Would you like to INVESTIGATE further, JUMP out the window, or CONTINUE? ')
    if lastInputFunction.lower() in('yes','search','investigate'):
      print('You walk closer to the window to get more information, but clumsily step on the broken glass. it cracks noisily, and you suddenly hear shuffling from your kitchen. \nThe intruder knows you are there.')
      Danger = Danger + 1
      kitchen()
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
      kitchen()
      
def kitchen ():
    print('\nSkillfully, you make your way into the kitchen. there is no obvious danger, so you may SEARCH more closely if you wish.')
    lastInputFunction = input('Do you want to search the kitchen? ')
    if lastInputFunction.lower() in('yes','search','investigate','identify','anything else'):
      print('Your attention is drawn to the kitchen knife holder, which stands empty. The intruder may be armed, but now you are prepared for it')
      Danger = Danger - 1
      phone()
    else:
      Danger = Danger + 2
      phone()

def phone ():  
  print('\nNext you slink into the dining room. on the wall you notice your landline, wall-mounted, battery-powered, still working home phone. you could dial up a number if you wish. ')
  phoneCall = input('what number would you like to call? ')
  if phoneCall.lower() in('911','police','authorities'):
    print('You dial in the number and let it ring out. The police should arrive to check it out. Help is on the way')
    Danger = Danger -1
    intruder()
  elif phoneCall.lower() in('pizza','little','caesars','dominos',"domino's",'door','dash'):
    print('The phone rings for a moment before the pizza delivery service responds. You start to order your favorite pizza, when from around the corner the intruder intrudes, asking for a large pepperoni and sausage.')
    print('Once the order is confirmed and paid for, the food is delivered and you and your new intrusive friend spend the rest of the night laughing, talking, and playing games.')
    print('SECRET ENDING UNLOCKED. PIZZA POWER!')
    exit()

  else:
    print('the number you call starts to ring, but before anyone answers...')
    intruder()
    
def intruder():
    print('\nSuddenly, the silhouette separates itself from the shadows of a hallway and approaches you. the intruder stands before you, and confrontation in inevitable.')
    lastInputFunction = input("The intruder approaches threateningly. You have to make you move. do you take an AGGRESSIVE action, and charge your foe, or do you take a DEFENSIVE action, and prepare to weather the intruder's assault")
    if lastInputFunction.lower() == 'defensive':
      print('You brace yourself and look for a chance to disarm the intruder!')
      Danger = Danger - 1
      fight_outcome()
    elif lastInputFunction.lower() == 'aggressive':
      print('You act on instinct, lunging for a first strike against the intruder!')
      Danger = Danger + 1
      fight_outcome()
    else:
     print('That action is not supported in this fight. your unpreparedness is your own undoing')
     Danger = Danger + 3
     fight_outcome()

def fight_outcome():
    
  if Danger >= 15:
    print('Unfortunately, the intruder had gotten the better of you. It was brave holding your own against them, but really you never stood a chance. maybe next time you will fare better.')
    print('GAME OVER: LOSS')
    exit()
  else:
    print('Triumphantly, you stand over your would-be killer. The intruder was successfully apprehended by your efforts, and you are named a hero in the news that very morning.')
    print('GAME OVER: OVERWHELMING VICTORY!')


print('You wake up suddenly to loud crash. You were sound asleep in the bedroom of your own home. Gradually, you come to your senses. The noise sounded like a window was broken near the living room.')
print('You have the option to DRESS YOURSELF, SEARCH the cabinets, and to PROCEED down the hallway.')
print("NOTE: taking certain actions will increase or decrease the DANGER level. Take caution to your decisions.")
print("NOTE: answer yes or no questions with a full 'yes' or 'no', and options are displayed in full caps.")



#flashlight gets mad at line 29 if i dont have this. its dumb, but true. " ' ' " IS EQUAL TO TRUE, SO I CHANGED TO FALSE. LINES 65 - 80 WORK NOW BUT ITS ONLY A TEMPORARY AND CRUDE FIX (line 26 explains the problem). WTF AM I MISSING.
FlashLight = False

# dress prompt and action.
if Danger >= 30:
    print('Oh no you wasted too much time and you were caught')
    print('Ending: Time Waster')
dress = input('\nYou notice you are wearing pajamas. would you like to get DRESSED? ')
if dress.lower() in('dress','yourself','myself','yes','dressed'):
        print('You take the time to dress yourself in something besides your pajamas.')
        Danger += 5
        hallway()
elif dress.lower() == 'no':
        search = input('\nWould you like to SEARCH the cabinets of your room?: ')
        if search.lower() == 'yes':
          FlashLightQuestion = input('Inside the drawer of one of your cabinets is a small flashlight. Do you TAKE it?: ')
        if FlashLightQuestion.lower() == 'TAKE':
            print('You take the flashlight.')
            FlashLight = True
            hallway()
        else:
            FlashLight = False
            hallway()
    
