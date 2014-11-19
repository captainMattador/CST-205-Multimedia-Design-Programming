
# Helper function to pick a picture file

def getPic():
  filename = pickAFile()
  return makePicture( filename )



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




# Function that puts together 3
# vector circles to represent a 
# snowman

def makeSnowMan(pic):
  addOvalFilled( pic, 100, 50, 50, 50, white)
  addOvalFilled( pic, 75, 100, 100, 100, white)
  addOvalFilled( pic, 50, 200, 150, 150, white)
  
  
# Function that copies over one image into another
# source is the image to be copied onto, target
# is the function to copie over, target x and y is 
# the desired location, removeColor is a color that 
# is not wanted and colorTolerance is an int of distance
# from removeColor

def pyCopy(source, target, targetX, targetY, removeColor, colorTolerance):
  
  sourceWidth = getWidth( source )
  sourceHeight = getHeight( source )
  targetWidth = getWidth( target )
  targetHeight = getHeight( target )
  
  for x in range( 0, sourceWidth ):
    for y in range( 0, sourceHeight ):
      pixel = getPixel( source, x, y )
      color = getColor( pixel )
      
      if x + targetX < targetWidth - 1 and y + targetY < targetHeight - 1:
        if distance( getColor(pixel), removeColor ) > colorTolerance: 
          setColor( getPixel( target, x + targetX, y + targetY ), color )
        
        
def cardOne():
  backgroundPic = getPic()
  turkey = getPic()
  border = getPic()
  removeColor = makeColor(255, 255, 255)
  fontColor = makeColor(83, 22, 22)
  myStyle = makeStyle(serif, italic+bold, 30)
  pyCopy(turkey, backgroundPic, 161, 146, removeColor, 20)
  pyCopy(border, backgroundPic, 0, 0, removeColor, 20)
  addTextWithStyle(backgroundPic, 200, 30, "Happy Thanksgiving", myStyle, fontColor)
  show( backgroundPic )
  writePictureTo(backgroundPic, "/Users/Captain/Desktop/thansgiving-card.jpg")
 

def cardTwo():
  backgroundPic = getPic()
  turkey2 = getPic()
  cornucopia = getPic()
  removeColor = makeColor(255, 255, 255)
  fontColor1 = makeColor(255, 255, 255)
  fontColor2 = makeColor(83, 22, 22)
  fontStyle1 = makeStyle(serif, italic+bold, 30)
  fontStyle2 = makeStyle(serif, italic+bold, 40)
  pyCopy(cornucopia, backgroundPic, 0, 112, removeColor, 30)
  pyCopy(turkey2, backgroundPic, 313, 188, removeColor, 30)
  addTextWithStyle(backgroundPic, 365, 30, "Happy", fontStyle1, fontColor1)
  addTextWithStyle(backgroundPic, 220, 60, "Thanksgiving", fontStyle2, fontColor2)
  betterBnW( backgroundPic )
  show( backgroundPic )
  writePictureTo(backgroundPic, "/Users/Captain/Desktop/thansgiving-card2.jpg")

