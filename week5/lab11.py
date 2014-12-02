

# Global variable defining rooms
rooms = ["Basement", "Kitchen", "Laundry Room", "Bedroom", "Foyer", "Dinning Room", "Living Room"]


def messages(msg):
  
  intro = """\n*** Welcome to \"Escape the Horror!\" A text based adventure game! ***\n
You've woken up in a damp basement and your head is foggy.
You cant quite remember how you've gotten here.
There is one flickering light that makes the scene all the more eeire.
You can feel the blood dripping from your head and see some flowing towards the drain in the center room.
Looking around you see a table with torture tools.
It's all coming back to you now. You remember the party in the woods when all of a sudden
you felt something smack against your head!
You can't remember much else, but visions of coming in and out of consiousness and the bits of pain.... and...
That scary looking man. He's not here now. He left you untied. He must have thought no way you would be waking up.
This might be your only chance! You have to make a run for it!\n"""
  
  instructions = """\n*** Game Instructions ***\n
You have to escape this house of horror.
You are not familiar with the house so you will have to take your chances.
In each room you will be given a description to act upon.
Type \"north\", \"south\", \"east\", or \"west\" to head in certain directions.
type \"pick up\" if there is an item available, and type \"use item\" to use the item.
Whatever you do, don't let the man find you!
At any time type \"help\" to see instructions again, or \"exit\" to end the game."""
  
  foyer = """\nIt looks like you are in the foyer. There's cobwebs everywhere!
The front door is right there but it's bolted shut and you need a key... Maybe that's a way out?
You can take the door way to the east, door way to the west, or go down the stairs to the north."""
  
  basement = """\nOh no! You're back in the basement and he heard the stairs creaking!
It looks like you're done for!"""

  kitchen = """\nYou are in the kitchen.
I don't see any knives anywhere. There is a key over on the table.
That might be something useful! 
There is a door to the north, a door to the west"""
  
  laundryRoom = """\nYou are in the laundry room. There's a bared up window to the north.
It's dusgusting in here and roaches are everywhere.
I doubt any laundry gets done in here.
Head through the doorway to the south or the door way to east"""

  bedroom = """\nYou are in the master bedroom.
The walls are covered in red paint that says \"the voices never stop!\"
All the windows are boarded up  and the only other object in here is the matress on the floor.
The stench is awful. 
You can head through the door to the east or the door to the north"""

  livingroom = """\nThis must be the living room.
The TV is playing home videos of a sad looking child!
There's empty medication bottles everywhere and no windows.
There's one locked and bolted door to the north. Maybe that's a way out.
You can head through the door to the west or the door to the south"""

  dinningroom = """\nThe dining room.
This has been the only place with actual furniture in it!
I doubt it gets used very often.
There's a lot of candles burning that are almost down to a nub.
You can head through the door to the east or the door to the west"""
  
  error = """Sorry, I didn't understand what you meant. Type another command."""
  
  if msg == "intro":
    printNow(intro)
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
  elif msg == "Dinning Room":
    printNow(dinningroom)
  elif msg == "Living Room":
    printNow(livingroom)
  else:
    printNow(error)


def getInput():
  return requestString("\nWhat direction would you like to go in?\nType help for instructions of quit to exit the game: ")


def endGame(results):
  printNow("\nThanks for playing!")



def changeLocations(currentLocation, direction):
  if currentLocation == "Basement" and direction == "south":
    return "Foyer"
  elif currentLocation == "Kitchen" and direction == "north":
    return "Laundry Room"
  elif currentLocation == "Kitchen" and direction == "east":
    return "Foyer"
  elif currentLocation == "Laundry Room" and direction == "south":
    return "Kitchen"
  elif currentLocation == "Laundry Room" and direction == "east":
    return "Dinning Room"
  elif currentLocation == "Bedroom" and direction == "north":
    return "Living Room"
  elif currentLocation == "Bedroom" and direction == "west":
    return "Foyer"
  elif currentLocation == "Foyer" and direction == "north":
    return "Basement"
  elif currentLocation == "Foyer" and direction == "west":
    return "Kitchen"
  elif currentLocation == "Foyer" and direction == "east":
    return "Bedroom"
  elif currentLocation == "Foyer" and direction == "south":
    printNow("\nYou need a key to exit this door.")
    return currentLocation
  elif currentLocation == "Dinning Room" and direction == "west":
    return "Laundry Room"
  elif currentLocation == "Dinning Room" and direction == "east":
    return "Living Room"
  elif currentLocation == "Living Room" and direction == "west":
    return "Dinning Room"
  elif currentLocation == "Living Room" and direction == "south":
    return "Bedroom"
  elif currentLocation == "Living Room" and direction == "north":
    printNow("\nYou need a key to exit this door.")
    return currentLocation
  else:
    printNow("""\nDamn! Can't go that way. Try again.""")
    return currentLocation
  

def getItem(currentLocation, items):
  if currentLocation == "Kitchen":
    items.append("key")
    printNow("\nThis is awesome! You have a key. It must go to something important!")
  else:
    printNow("\nThere's no items in this room that would be useful.")
  

def checkInventory(items, item):
  for i in range(0, len(items)):
    if items[i].lower() == item.lower():
      return true
  return false


def useAnItem(currentLocation, items):
  printNow("\nYour current inventory includes:")
  printNow(items)
  item = requestString("\nType the name of the item you would like to use or nevermind to continue exploring.")
  if item == "nevermind":
    return
  else:
    hasItem = checkInventory(items, item)
    if hasItem:
      if item == "key" and currentLocation == "Living Room":
        printNow("\nYes! We'r getting out of here!")
      elif item == "key" and currentLocation == "Foyer":
        printNow("\nNO! It doesn't seem to go to any of these bolts!.")
      else:
        printNow("\nThere's no use for this item in here")
    else:
      printNow("\nSorry! You don't currently have an item like that.")


def playGame():

  gameOver = false
  results = false
  items = []
  currentLocation = rooms[0]
  
  messages("intro")
  messages("instructions")
  messages(currentLocation)
  
  while not(gameOver):
    userInput = getInput()
    if userInput == "exit":
      gameOver = true
      endGame(results)
    elif userInput == "help":
      messages("instructions")
    else:
      if userInput == "pick up":
        getItem(currentLocation, items)
      elif userInput == "use item":
        useAnItem(currentLocation, items)
      else:
        currentLocation = changeLocations(currentLocation, userInput)
        messages(currentLocation)


playGame()
