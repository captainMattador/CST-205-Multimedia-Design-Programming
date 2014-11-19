

# Helper function to pick a picture file

def getPic():
   return makePicture(pickAFile())


# takes a picture file represented as pic
# and sets tho blue pixels to 0
   
def noBlue(pic):
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    setBlue(p,0)


# takes a picture file represented as pic
# and a percentage to decreese red by

def lessRed(pic, percentage):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r - r*(percentage/100))


# takes a picture file represented as pic
# reduces the red by 50 percent

def halfRed(pic):
  lessRed(pic, 50)


# takes a picture file represented as pic
# and a percentage to Increese red by

def moreRed(pic, percentage):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    if r + r*(percentage/100) < 255:
      setRed(p, r + r * (percentage/100))
    else:
      setRed(p,255)


# takes a picture file represented as pic
# and gives the picture a pinkish overtone

def roseColoredGlasses(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setGreen(p, r*.50)
    setBlue(p, r*.85)


# takes a picture file represented as pic
# and lightens all the pixles in the pic
    
def lightenUp(pic):
  pixels = getPixels(pic)
  for p in pixels:
    newColor = makeLighter(getColor(p))
    setColor(p,newColor)


# takes a picture file represented as pic
# and turns each pixel to the opposite
# to create a negative
        
def makeNegative(pic):
  pixels = getPixels(pic)
  for p in pixels:
    negRed = 255-getRed(p)
    negGreen = 255-getGreen(p)
    negBlue = 255-getBlue(p)
    newColor = makeColor(negRed, negGreen, negBlue)
    setColor(p, newColor)


# takes a picture file represented as pic
# and turns it into black and white
# by finding the average of rg,b, in each pixel

def BnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    average = (r+g+b)/3
    setRed(p,average)
    setBlue(p,average)
    setGreen(p,average)


# BetterBnW takes a picture as parameter
# and turns the image black and white based
# on the each pixels luminance

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    newColor = getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.114
    setRed(p, newColor)
    setBlue(p, newColor)
    setGreen(p, newColor)
    
    