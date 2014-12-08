


# Matthew Bozelka - Lab Number 8
# Peer Partners - Julia Diliberto, Robert Contreras, Ryan Doherty



# main function that handles most of the game logic 
def startGame( correctPhrase, numOfTrys ):
  incorrectGuesses = []
  correctGuesses = []
  correctPhraseLength = lenghtWithNoDupes(correctPhrase)
  while numOfTrys > 0:
    guess = requestString("Guess a letter: ")
    if len(guess) == 0 or len(guess) > 1 or guess.isdigit() or guess == " " or not guess.isalpha():
      printNow( "\nLetters and single characters only please!" ) 
    elif inArray( guess, incorrectGuesses) or inArray( guess, correctGuesses):
      printNow( "\nYou already guess that, try again" )
    else:
      if guess.lower() in correctPhrase.lower():
        correctGuesses.append(guess)
        printResponseToGuess( true, correctPhrase, correctGuesses, incorrectGuesses, numOfTrys )
        if len(correctGuesses) == correctPhraseLength:
          printNow("\nCongratulations you win!")
          break
      else:
        incorrectGuesses.append(guess)
        numOfTrys -= 1
        printResponseToGuess( false, correctPhrase, correctGuesses, incorrectGuesses, numOfTrys )
  else:
    printNow( "\nSorry, you lose.  Better luck next time!" )

    

# helper function that prints 
# the game instructions
def gameDescription():
  printNow( "In this game you have to guess the correct letters in the unknown phrase. If you guess incorrectly 6 times the game will be over" )
  
  
  

# helper function that checks if
# a char is in a specific array 
def inArray( item, arr ):
  for i in range(0, len(arr)):
    if arr[i].lower() == item.lower():
      return true
  return false
    
 
  


# helper function that removes dupe
# chars in string and returns the length
# of original characters (and no spaces)  
def lenghtWithNoDupes(string):
  length = 0
  tempArr = []
  for char in string:
    if char != " " and not inArray( char, tempArr ):
      tempArr.append(char)
      length += 1
  return length
  
  


# helper function that prints out
# the array of incorrect guess
def printIncorrect( arr ):
  printString = ""
  for char in arr:
    printString = printString + char
  printNow( printString )
  
  



 
# helper function that prints out the current
# progress based on currently correct guesses 
def printProgress( correctPhrase, correctGuesses ):
  printString = ""
  for char in correctPhrase:
    if char == " " or inArray( char, correctGuesses ):
      printString = printString + char
    else:
      printString = printString + "_ "
  printNow( printString )
  





# helper function that prints
# the response to a correct
# or incorrect question
def printResponseToGuess( wasCorrect, correctPhrase, correctGuesses, incorrectGuesses, numOfTrys ):
  if wasCorrect:
    printNow( "\nCorrect!" )
  else:
    printNow( "\nIncorrect!" )
  printNow( "Word so far:" )
  printProgress( correctPhrase, correctGuesses )
  printNow( "Incorrect guesses:" )
  printIncorrect( incorrectGuesses )
  printNow( "You have used %s of six guesses" % ( 6 - numOfTrys ) )
  





# this initializes the game
# you can change the number
# of trys, as well as the word/phrase
# to guess here
def hangMan():
  correctPhrase = "Hello wolrd"
  numOfTrys = 6;
  gameDescription()
  startGame( correctPhrase, numOfTrys )
  
  