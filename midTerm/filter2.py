


def getPic():
  return makePicture( pickAFile() )



# takes a picture file represented as pic
# and lightens all the pixles in the pic
def lightenUp(pic):
  pixels = getPixels(pic)
  for p in pixels:
    newColor = makeLighter(getColor(p))
    setColor(p,newColor)
  
  
  
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
    
def yellowing( pic ):
  betterBnW(pic)
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
      pixel = getPixel(pic, x, y)
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      setRed( pixel, r * .92 )
      setGreen( pixel, g * .91 )
      setBlue( pixel, b * .73 )

      
def addDistress(distress, pic, distressColor ):
  for x in range( 0, getWidth( pic ) ):
    for y in range( 0, getHeight( pic ) ):
      if distance( getColor( getPixel( distress, x, y ) ), makeColor(0, 0, 0) ) < 10:
        setColor( getPixel( pic, x, y ), distressColor )
      elif distance( getColor( getPixel( distress, x, y ) ), makeColor(255, 0, 0) ) < 150:
        setColor( getPixel( pic, x, y ), makeColor(255, 0, 0) )
    
    
    
def oldTimey(pic):
  dust = makePicture( "/Users/Captain/Desktop/filters/dust.jpg" )
  grungeBKG = makePicture( "/Users/Captain/Desktop/filters/grungeBKG.jpg" )
  addDistress(grungeBKG, pic, makeColor(0, 0, 0) )
  addDistress(dust, pic, makeColor(0, 0, 0) )
  yellowing( pic )
  lightenUp(pic)
  lightenUp(pic)
  return pic 
  
  
  
pic = getPic()
oldTimey(pic)
show(pic)