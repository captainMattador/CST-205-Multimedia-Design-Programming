
import random


# craps game messages
messages = dict()

messages['welcome'] = '''\n*******************************
Welcome to the Craps Table
*******************************\n'''

messages['roll'] = '''\n*******************************
Rolling the dice!
*******************************\n'''

messages['win-message-first-roll'] = '''\n*******************************
Wow you got the touch tonight!
*******************************\n'''


messages['win-message-on-point'] = '''\n*******************************
You're on point tonight!
*******************************\n'''

messages['lose-message-first-roll'] = '''\n*******************************
Ouch... That was unlukcy!
*******************************\n'''

messages['lose-message-on-point'] = '''\n*******************************
Man... your luck is up!
*******************************\n'''




# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: %d" % msg)
  
  
      
# a single rolled die
def die():
  return random.randrange(1, 7, 1)
    
    
# the total pf two dice rolled
def rollDice():
  return die() + die()
  
  

# call the function to play the craps game
def crapsGame():
  
  gameOver = false
  rollCount = 0
  printNow(messages['welcome'])
  printNow(messages['roll'])
  
  # first roll
  point = rollDice()
  rollCount += 1
  printNow("\n%s Total rolls. This rolls total %s\n" % (rollCount, point))
    
  if point == 7 or point == 11:
    printNow(messages['win-message-first-roll'])
  elif point == 2 or point == 3 or point == 12:
    printNow(messages['lose-message-first-roll'])
  else:
    while not gameOver:
      roll = rollDice()
      rollCount += 1
      printNow("\n%s Total rolls. This rolls total %s\n" % (rollCount, roll))
      if roll == point:
        printNow(messages['win-message-on-point'])
        gameOver = true
      elif roll == 7:
        printNow(messages['lose-message-on-point'])
        gameOver = true

   
  