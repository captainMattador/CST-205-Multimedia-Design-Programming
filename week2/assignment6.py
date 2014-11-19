
# Helper function to pick a picture file

def getPic():
   return makePicture(pickAFile())



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
# a desired color to replace the red eyes in the pic
# and a tolerance to check against
# and attemps the remove the red eyes in the pic

def fixRedEyes( pic, desiredColor, tolerance ):

  searchForColor = makeColor( 158, 40, 12);
  
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
      
      pixel = getPixel(pic, x, y)
      
      if distance( getColor(pixel), red ) < tolerance:
        setColor( pixel, desiredColor )
  


# takes a picture as parameter
# turns the pic black and white
# and then creates a sepia tone color

def sepiaTone( pic ):
  
  pic = betterBnW(pic)
  
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
    
      pixel = getPixel(pic, x, y)
      r = getRed(pixel)
      b = getBlue(pixel)
      
      if r < 63:
        setRed( pixel, r * 1.1 )
        setBlue( pixel, b * 0.9 )
        
      elif r > 62 and r < 192:
        setRed( pixel, r * 1.15 )
        setBlue( pixel, b * 1.15 )
        
      else:
        if r * 1.08 > 255:
          setRed( pixel, 255 )
        else:
          setRed( pixel, r * 1.08 )
        setBlue( pixel, b * 0.93 )
        
  return pic
  
  
# takes a picture as parameter
# and creates an artsy look by
# limiting the amount of tones in
# r, g, and b

def Artify( pic ):
  
  for x in range( 0, getWidth(pic) ):
    for y in range(0, getHeight(pic) ):
    
      pixel = getPixel(pic, x, y)
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      if r < 64:
        setRed( pixel, 31 )
        
      elif r > 63 and r < 128:
        setRed( pixel, 95 )
        
      elif r > 127 and r < 192:
        setRed( pixel, 159 )
        
      else:
        setRed( pixel, 223 )
        
        
        
      if b < 64:
        setBlue( pixel, 31 )
        
      elif b > 63 and b < 128:
        setBlue( pixel, 95 )
        
      elif b > 127 and b < 192:
        setBlue( pixel, 159 )
        
      else:
        setBlue( pixel, 223 )
        
        
        
      if g < 64:
        setGreen( pixel, 31 )
        
      elif g > 63 and g < 128:
        setGreen( pixel, 95 )
        
      elif g > 127 and g < 192:
        setGreen( pixel, 159 )
        
      else:
        setRed( pixel, 223 )
        
  
# takes a source image that is on a green screen,
# and a background image
# and attempts to remove the green screen to reveal the
# background image
  
def chromakey(sourceImage, bkgImage):
  
  screen = makeColor( 105, 244, 3 )
  sourceWidth = getWidth(sourceImage)
  sourceHeight = getHeight(sourceImage)
  bkgWidth = getWidth(bkgImage)
  bkgHeight = getHeight(bkgImage)
  
  for x in range( 0, sourceWidth ):
    for y in range(0, sourceHeight ):
    
      sourcePixel = getPixel( sourceImage, x, y)
      sourceColor = getColor( sourcePixel )
      
      if distance( sourceColor, screen ) < 50:
        setColor( sourcePixel,  getColor( getPixel( bkgImage, x, y) ) )
        
  


  