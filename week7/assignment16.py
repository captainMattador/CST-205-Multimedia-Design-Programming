

import urllib




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





# Scrapes abduzeedo and returns a list of headlines
def scrapeHeadLines():
  
  filehandle = urllib.urlopen('http://abduzeedo.com/')
  fileToText = filehandle.read()
  fileToText = fileToText.split('\n')
  headLines = []
  
  for line in fileToText:
    if line.find('<h2 class="title">') != -1:
      headLines.append(line)
 
  return headLines




# writes headlines scrapped from abduzeedo to another html file
def createFile():
  
  getHeadLines = ''.join(scrapeHeadLines())
  Html_file= open("/Users/Captain/GitHub/CST-205-Multimedia-Design-Programming/week7/new-rss.html","w")
  Html_file.write(html('My Rss Feed', getHeadLines))
  Html_file.close()

  

createFile()
  
  
  