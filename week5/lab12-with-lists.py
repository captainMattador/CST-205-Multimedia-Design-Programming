
# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: " + msg)


# handles all the messaging for the game. Checks certain
# parameters to determine what the room should say.
def messages(msg, gameVars):
  
  # intro
  intro = """\n*** Welcome to \"Escape the Horror!\" A text based adventure game! ***\n
You've woken up in a damp basement and your head is foggy.
You cant quite remember how you've gotten here.
There is one flickering light that makes the scene all the more eeire.
You can feel the blood dripping from your head and see some flowing towards the drain in the center room.
Looking around you see a table with torture tools.
It's all coming back to you now. You remember the party in the woods when all of a sudden
you felt something smack against your head!
You can't remember much else, but visions of coming in and out of consiousness and the bits of pain.... and...
That scary looking man. He's not here now. He left you untied, but your hands are cuffed. 
He must have thought there was no way you would be waking up.
This might be your only chance! You have to make a run for it!\n"""
  
  # instructions
  instructions = """\n*** Game Instructions ***\n
You have to escape this house of horror.
You are not familiar with the house so you will have to take your chances.
There are a few items you will need to make your escape, so keep your eyes open!
In each room you will be given a description to act upon.
Type \"north\", \"south\", \"east\", or \"west\" to head in certain directions.
type \"pick up\" if there is an item available, and type \"use item\" to use the item.
Whatever you do, don't let the man find you!
At any time type \"help\" to see instructions again, or \"exit\" to end the game."""
  
  # statements for the basement
  if not gameVars["hasPick"]:
    begining = """\nYou're currently in the basement and your hands are cuffed.
There is a small item on the table that might be usable as a pick.
It looks like there is only one way out.
You're going to have to take the stairs to the south."""
  elif gameVars["hasPick"] and gameVars["stillCuffed"]:
    begining = """\nYou're currently in the basement and your hands are cuffed.
It looks like there is only one way out.
You're going to have to take the stairs to the south."""
  else:
    begining = """\nYou're currently in the basement.
It looks like there is only one way out.
You're going to have to take the stairs to the south."""
   
   # statements for the foyer
  foyer = """\nIt looks like you are in the foyer. There's cobwebs everywhere!
The front door is right there but it's bolted shut and you need a key... Maybe that's a way out?
You can take the door way to the east, door way to the west, or go down the stairs to the north."""
  
  # statements for the basement
  basement = """\nOh no! You're back in the basement and he heard the stairs creaking!
It looks like you're done for!"""
  
  # statements for the kitchen
  if not gameVars["jarBorken"]:
    kitchen = """\nYou are in the kitchen.
I don't see any knives anywhere. There is a jar on the top cabinet.
You can't reach it though. If only you had a stick.
There is a door to the north, a door to the east"""
  elif not gameVars["hasKey"] and gameVars["jarBorken"]:
    kitchen = """\nYou are in the kitchen.
I don't see any knives anywhere. You smashed the jar and a key fell out.
I bet that will be useful.
There is a door to the north, a door to the east"""
  elif gameVars["hasKey"]:
    kitchen = """\nYou are in the kitchen.
I don't see any knives anywhere.
There is a door to the north, a door to the east"""
  
  # statements for the laundry room
  laundryRoom = """\nYou are in the laundry room. There's a bared up window to the north.
It's dusgusting in here and roaches are everywhere.
I doubt any laundry gets done in here.
Head through the doorway to the south or the door way to east"""
  
  # statements for the bedroom
  if not gameVars["hasStick"]:
    bedroom = """\nYou are in the master bedroom.
The walls are covered in red paint that says \"the voices never stop!\"
The stench is awful.
All the windows are boarded up  and the only other object in here is the matress on the floor.
No wait! There's a stick on the otherside of the bed. It's no knife, but it's something.
There's a small light coming from the south... I woder what that is?
You can head through the door to the east, the door to the north, or explore."""
  else:
    bedroom = """\nYou are in the master bedroom.
The walls are covered in red paint that says \"the voices never stop!\"
The stench is awful.
All the windows are boarded up  and the only other object in here is the matress on the floor.
There's a small light coming from the south... I woder what that is?
You can head through the door to the east, the door to the north, or explore."""
  
  # statements for the livingroom
  livingroom = """\nThis must be the living room.
The TV is playing home videos of a sad looking child!
There's empty medication bottles everywhere and no windows.
There's one locked and bolted door to the north. Maybe that's a way out.
You can head through the door to the west or the door to the south"""
  
  # statements for the diningroom
  diningroom = """\nThe dining room.
This has been the only place with actual furniture in it!
I doubt it gets used very often.
There's a lot of candles burning that are almost down to a nub.
You can head through the door to the east or the door to the west"""
  
  # statements for the hidden room
  hiddenRoom = """\nOh this is just a closet... wait what's that noise?
Oh no... it's him! He's looking aroud as if he knows something is wrong!
He's... he's sniffing the air? Oh thank God, he's leaving the room.
That was a close one. The only way out is to head north back into the 
bedroom."""
  
  error = """Sorry, I didn't understand what you meant. Type another command."""
  
  if msg == "intro":
   showInformation(intro)   
  elif msg == "instructions":
    printNow(instructions)  
  elif msg == "Basement":
    printNow(basement)  
  elif msg == "Kitchen":
    printNow(kitchen)  
  elif msg == "Laundry Room":
    printNow(laundryRoom)
  elif msg == "Bedroom":
    printNow(bedroom)  
  elif msg == "Foyer":
    printNow(foyer) 
  elif msg == "Dining Room":
    printNow(diningroom)  
  elif msg == "Living Room":
    printNow(livingroom)  
  elif msg == "Starting Point":
    printNow(begining)   
  elif msg == "Hidden Room":
    printNow(hiddenRoom)
  else:
    printNow(error)



# helper function to get input from the user
def getInput():  
  return requestString("""\nWhat would you like to do  Pick up an item, use an item, or go in a specific direction  Type help for instructions or quit to exit the game:""")




# checks the direction selected
# and retruns the room that would be entered
def changeLocations(currentLocation, direction):
  # debugger(currentLocation)
  # debugger(direction)
  if currentLocation == "Starting Point" and direction == "south":
    return "Foyer"  
  elif currentLocation == "Basement" and direction == "south":
    return "Foyer"   
  elif currentLocation == "Kitchen" and direction == "north":
    return "Laundry Room"   
  elif currentLocation == "Kitchen" and direction == "east":     
    return "Foyer"  
  elif currentLocation == "Laundry Room" and direction == "south":     
    return "Kitchen"   
  elif currentLocation == "Laundry Room" and direction == "east":
    return "Dining Room"  
  elif currentLocation == "Bedroom" and direction == "north":
    return "Living Room"  
  elif currentLocation == "Bedroom" and direction == "west":
    return "Foyer"   
  elif currentLocation == "Bedroom" and direction == "south":
    return "Hidden Room"
  elif currentLocation == "Hidden Room" and direction == "north":
    return "Bedroom"
  elif currentLocation == "Foyer" and direction == "north":
    return "Basement"
  elif currentLocation == "Foyer" and direction == "west":
    return "Kitchen"
  elif currentLocation == "Foyer" and direction == "east":
    return "Bedroom"
  elif currentLocation == "Foyer" and direction == "south":
    printNow("\nYou need a key to exit this door.")
    return currentLocation
  elif currentLocation == "Dining Room" and direction == "west":
    return "Laundry Room"
  elif currentLocation == "Dining Room" and direction == "east":
    return "Living Room"
  elif currentLocation == "Living Room" and direction == "west":
    return "Dining Room"
  elif currentLocation == "Living Room" and direction == "south":
    return "Bedroom"
  elif currentLocation == "Living Room" and direction == "north":
    printNow("\nYou need a key to exit this door.")
    return currentLocation
  else:
    printNow("""\nDamn! Can't go that way. Try again.""")
    return currentLocation
    
    
    
# end game function. Checks if you won the game or lost
def endGame(winner, userName):
  if winner:
    showInformation("\nWOW %s! You made it out! You live to see another day." % userName )
  else:
    showInformation("\nDarn it %s! You were caught by the killer! Your chances were slim anyways." % userName)  



# function that handles getting the items. checks for required variables
# it returns the item gotten if one is able to be gotten
def getItem(currentLocation, items, gameVars):
  # debugger(currentLocation)
  # debugger(items)
  # debugger(hasStick)
  # debugger(hasKey)
  # debugger(hasPick)
  # debugger(jarBorken)
  if currentLocation == "Starting Point" and not gameVars["hasPick"]:
    items.append("pick")
    printNow("\nNice! You can use this pick to undo your handcuffs!")
    return "pick"
  elif currentLocation == "Kitchen" and gameVars["jarBorken"] and not gameVars["hasKey"]:
    items.append("key")
    printNow("\nThis is awesome! You have a key. It must go to something important!")
    return "key"
  elif currentLocation == "Bedroom" and not gameVars["hasStick"]:
    items.append("stick")
    printNow("\nI'm sure this stick will be useful")
    return "stick"
  else:
    printNow("\nThere's no items in this room that would be useful.")
    return "undefined"

  

# function that handles if a user wants to use an item. 
# often checks for certain variables
def useAnItem(currentLocation, items, gameVars):
  # debugger(currentLocation)
  # debugger(items)
  # debugger(hasStick)
  # debugger(hasKey)
  # debugger(stillCuffed)
  printNow("\nYour current inventory includes:")
  printNow(items)
  item = requestString("\nType the name of the item you would like to use or nevermind to continue exploring.")
  if item == "nevermind":
    return "undefined"
  else:
    hasItem = checkInventory(items, item)
    if hasItem:
      if item == "pick":
        removeInventory(items, item)
        printNow("\nPerfect! now your hands are free to use!")
        return "pick"
      elif item == "key" and currentLocation == "Living Room" and not gameVars["stillCuffed"]:
        removeInventory(items, item)
        printNow("\nYes! We'r getting out of here!")
        return "key"
      elif item == "key" and currentLocation == "Living Room" and gameVars["stillCuffed"]:
        printNow("\nCrap... You can't reach the lock with your hands still tied")
        return "undefined"
      elif item == "key" and currentLocation == "Foyer":
        printNow("\nNO! It doesn't seem to go to any of these bolts!.")
        return "undefined"
      elif item == "stick" and currentLocation == "Kitchen" and not gameVars["hasKey"]:
        printNow("\nGreat job! You knocked down the jar! And look, there was a key in there!")
        return "stick"
      else:
        printNow("\nThere's no use for this item in here")
        return "undefined"
    else:
      printNow("\nSorry! You don't currently have an item like that.")
      return "undefined" 
    




# removes an item from the array of items
def removeInventory(items, item):
  items.remove(item)
  



# checks if item used is in the items array
def checkInventory(items, item):
  for i in range(0, len(items)):
    if items[i].lower() == item.lower():
      return true
  return false
  
  
  
  
# starts the game and handles the main logic   
def playGame():
  
  gameVars = dict()
  gameVars["gameOver"] = false        # determines if game is over or not
  gameVars["winner"] = false          # var for winnder or loser
  gameVars["leftBasement"] = false    # var true if left basement for first time
  gameVars["itemUsed"] = false        # captures which item gets used
  gameVars["stillCuffed"] = false      # checks if still handcuffed
  gameVars["hasKey"] = false          # true if you've found the key
  gameVars["hasStick"] = false        # true if you've found the stick
  gameVars["hasPick"] = false         # true if you've foudn the pick
  gameVars["jarBorken"] = false       # true if you've broken the jar
  items = []              # array of found items
  currentLocation = "Starting Point"
  userName = ""
  
  
  messages("intro", gameVars)
  messages("instructions", gameVars)
  userName = requestString("\nEnter the name of your character:")
  messages(currentLocation, gameVars)
  
  while not(gameVars["gameOver"]):
    userInput = getInput()
    if userInput == "exit":
      gameVars["gameOver"] = true
      endGame(gameVars["winner"], userName)
    elif userInput == "help":
      messages("instructions", gameVars)
    else:
      if userInput == "pick up":
        item = getItem(currentLocation, items, gameVars)
        # debugger(item)
        if item == "stick":
          gameVars["hasStick"] = true
        elif item == "key":
          gameVars["hasKey"] = true
        elif item == "pick":
          gameVars["hasPick"] = true
      elif userInput == "use item":
        itemUsed = useAnItem(currentLocation, items, gameVars)
        # debugger(itemUsed)
        if itemUsed == "key":
          gameVars["gameOver"] = true
          gameVars["winner"] = true
          endGame(gameVars["winner"], userName)
        elif itemUsed == "pick":
          gameVars["stillCuffed"] = false
        elif itemUsed == "stick":
          gameVars["jarBorken"] = true
      else:
        currentLocation = changeLocations(currentLocation, userInput)
        # debugger(currentLocation)
        if currentLocation == "Basement" and gameVars["leftBasement"]:
          gameVars["gameOver"] = true
          messages(currentLocation, gameVars)
          endGame(gameVars["winner"], userName)
        else:
          gameVars["leftBasement"] = true
          messages(currentLocation, gameVars)



# start the game when program loads
playGame()

