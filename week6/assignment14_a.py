


# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: %d" % msg)
  
  

def greenEggsAndHam():
  
  uniqueWordCounter = dict()         # dictionary to count unu=ique words
  numOfUniqueWords = 0               # total number of unique words
  totalWords = 0                     # total number of words
  mostUsedWord = ""                  # most used word 
  
  # get file to read
  file = open("/Users/Captain/GitHub/CST-205-Multimedia-Design-Programming/week6/eggs.txt", "rt")
  fileText = file.read()
  file.close()
  
  # make text all lower, replace the dashes then split into an array
  fileText = fileText.lower().replace("-", " ").split()
  totalWords = len(fileText)
  
  for word in fileText:
    if word in uniqueWordCounter:
      uniqueWordCounter[word] += 1
    else:
      uniqueWordCounter[word] = 1
      numOfUniqueWords += 1
  
  mostUsed = 0
  for word in uniqueWordCounter:
    if uniqueWordCounter[word] > mostUsed:
      mostUsedWord = word
      mostUsed = uniqueWordCounter[word]
      
  showInformation("There is a tototal of %s unique words in Green Eggs and Ham" % numOfUniqueWords)
  
  for key, value in uniqueWordCounter.iteritems():
      print "%s : %s" % (key, value)

    