

def getPic():
  return makePicture( pickAFile() )
  


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
    
# takes a picture as parameter
# turns the pic black and white
# and then creates a sepia tone color

def goldTone( pic ):
  betterBnW(pic)
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
      pixel = getPixel(pic, x, y)
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      setRed( pixel, r * .64 )
      setGreen( pixel, g * .57 )
      setBlue( pixel, b * .37 )
        
  
def addLogo(logo, pic, targetX, targetY):
  for x in range( 0, getWidth( logo ) ):
    for y in range( 0, getHeight( logo ) ):
      if x + targetX < getWidth( pic ) - 1 and y + targetY < getHeight( pic ) - 1:
        setColor( getPixel( pic, x + targetX, y + targetY ), getColor( getPixel( logo, x, y ) ))
             

def addBorder(pic):
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
      if x <= 10 or x >= getHeight(pic) - 10 or y <= 10 or y >= getHeight(pic) - 10:
        setColor( getPixel( pic, x, y ), makeColor(0, 51, 102) )
        

def csumberize(pic):
  logo = makePicture( "/Users/Captain/Desktop/filters/logo.jpg" )
  csumbGold = makeColor(164, 146, 96)
  csumbBlue = makeColor(0, 53, 106)
  font = makeStyle(serif, italic+bold, 40)
  goldTone(pic)
  addBorder(pic)
  addRectFilled( pic, 0, 480, 640, 125, makeColor(255, 255, 255) )
  addRectFilled( pic, 0, 500, 640, 3, csumbBlue )
  addRectFilled( pic, 0, 506, 640, 3, csumbGold )
  addRectFilled( pic, 0, 579, 640, 3, csumbGold )
  addRectFilled( pic, 0, 585, 640, 3, csumbBlue )
  addTextWithStyle(pic, 292, 560, "Class of 2016!", font, csumbBlue)
  addTextWithStyle(pic, 290, 558, "Class of 2016!", font, csumbGold)
  addLogo(logo, pic, 0, 485)
  
  return pic 
  

  