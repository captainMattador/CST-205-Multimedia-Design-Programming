

import urllib



# debugger function to 
# know in code if it was meant to be a print or for debuggin
def debugger(msg):
  printNow("debugger: %d" % msg)





#pre condition: Takes a title and a bodyHTML attribute
#returns a full html page of text and replaces the title and body with the attributes
def html(title, bodyHTML):
  return '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>%s</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
      %s
    </body>
</html>''' % (title, bodyHTML)





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
      
  #showInformation("There is a tototal of %s unique words in Green Eggs and Ham" % numOfUniqueWords)
  
  return uniqueWordCounter





# creates the body copy out of the words from Green Eggs and Ham
def createFile():
  
  words = greenEggsAndHam()
  htmlToAdd = ""
  frequencies = {
    "0-10" : "color:#3d3d3d; font-size:12px; font-weight:100",
    "11-20" : "color:#a53434; font-size:14px; font-weight:200",
    "21-30" : "color:#5a1313; font-size:16px; font-weight:300",
    "31-40" : "color:#6056e6; font-size:18px; font-weight:400",
    "41-50" : "color:#272086; font-size:20px; font-weight:500",
    "51-60" : "color:#d5e05c; font-size:22px; font-weight:600",
    "61-70" : "color:#e05cd2; font-size:24px; font-weight:700",
    "71-80" : "color:#5cd8e0; font-size:26px; font-weight:800",
    "81-90" : "color:#1c4143; font-size:28px; font-weight:900",
    "91-100" : "color:#076221; font-size:30px; font-weight:900"
  }
 
  for key, value in words.iteritems() :
    if value < 11:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["0-10"], key )
    elif value > 10 and value < 21:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["11-20"], key )
    elif value > 20 and value < 31:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["21-30"], key )
    elif value > 30 and value < 41:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["31-40"], key )
    elif value > 40 and value < 51:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["41-50"], key )
    elif value > 50 and value < 61:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["51-60"], key )
    elif value > 60 and value < 71:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["61-70"], key )
    elif value > 70 and value < 81:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["71-80"], key )
    elif value > 80 and value < 91:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["81-90"], key )
    elif value > 90 and value < 101:
      htmlToAdd = htmlToAdd + "<p style=\"%s\">%s</p>" % ( frequencies["91-100"], key )
  
  Html_file= open("/Users/Captain/GitHub/CST-205-Multimedia-Design-Programming/week7/green-eggs-and-ham-analysis.html","w")
  Html_file.write(html("Green Eggs and Ham Analysis", htmlToAdd))
  Html_file.close()




createFile()
  