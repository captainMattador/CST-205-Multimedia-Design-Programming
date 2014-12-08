


# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: %d" % msg)
  


def extract(text, start, end):
  
  dictOfFound = dict()
  record = false
  count = 0
  
  for word in text:
    if word == start:
      record = true
      count += 1
      dictOfFound[count] = []
    elif word == end:
      record = false
    elif record:
      dictOfFound[count].append(word)
      
  return dictOfFound
      
      
      
      
def removeSpecialChars(string):
  html_escape_table = {
     "&#8230;": "...",
     "&nbsp;": " "
  }

  for key, value in html_escape_table.iteritems():
    string = string.replace(key, value)

  return string
  
      
def makeHeadlines():
  file = open("/Users/Captain/GitHub/CST-205-Multimedia-Design-Programming/week6/index.html","rt")
  fileToText = file.read() 
  fileToText = fileToText.split()
  finalDict = dict()
  firstExtract = dict()
  secondExtract = dict()
  

  firstExtract = extract(fileToText, "class=\"archive_title\"", "</h3>")
  
  for i in firstExtract:
    secondExtract[i] = extract(firstExtract[i], "rel=\"bookmark\">", "</a>")
  
  headlineCount = 0
  for i in secondExtract:
    for j in secondExtract[i]:
      finalDict[headlineCount] = secondExtract[i][j]
      headlineCount += 1
  
  
  print "\n*** Otter Realm Breaking News! ****"
  for i in finalDict:
    headline = ""  
    for word in finalDict[i]:
      headline = headline + word + " "
    headline = removeSpecialChars(headline)
    print headline
      



    