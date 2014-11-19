

# Helper function to pick a picture file

def getPic():
  return makePicture(pickAFile())


# BetterBnW takes a picture as parameter
# and turns the image black and white based
# on the each pixels luminance

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    luminance = getLuminance(p)
    setRed(p, luminance)
    setBlue(p, luminance)
    setGreen(p, luminance)


# Helper function that retruns the
# luminance of a pixel

def getLuminance(pixel):
  return getRed(pixel)*0.299 + getGreen(pixel)*0.587 + getBlue(pixel)*0.114


# line drawing takes a picture file represented as pic
# and an int represented as tolerance. The function then turns
# pic into something that looks like a line drawing

def lineDrawing(pic, tolerance):
  
  betterBnW(pic)
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  for x in range( 0, picWidth ):
    for y in range( 0, picHeight ):
      currentPixel = getPixel(pic, x, y)
      rightPixel = None
      belowPixel = None
      
      if x == picWidth - 1:
        rightPixel = getPixel(pic, x, y)
      else:
        rightPixel = getPixel(pic, x + 1, y)
        
      if y == picHeight - 1:
        belowPixel = getPixel(pic, x, y)
      else:
        belowPixel = getPixel(pic, x, y + 1)
      
      currentPixelLum = getLuminance(currentPixel)
      belowPixelLum = getLuminance(belowPixel)
      rightPixelLum = getLuminance(rightPixel)
      
      if abs( currentPixelLum - belowPixelLum ) < tolerance and abs( currentPixelLum - rightPixelLum ) < tolerance:
        setColor( currentPixel, black )
      else:
        setColor( currentPixel, white )
  
  
  
  
  

