

# Helper function to pick a picture file

def getPic():
   return makePicture(pickAFile())



# takes a picture file represented as pic
# and paints half the pic lighter

def halfBetter( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  for x in range( 0 , picWidth/2 ):
    for y in range( 0 , picHeight ):
      pixel = getPixel( pic, x, y )
      color = makeLighter( getColor( pixel ) )
      setColor( pixel, color )

   return pic


# takes a picture file represented as pic
# and mirros the image on the x axis
  
def mirrorX( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  for x in range( 0 , picWidth/2 ):
    for y in range( 0 , picHeight ):
      pixel = getPixel( pic, x, y )
      color = getColor( pixel )
      setColor( getPixel( pic, picWidth - 1 - x , y ), color )

   return pic


# takes a picture file represented as pic
# and mirros the image from the top down
  
def mirrorY( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  for y in range( 0 , picHeight/2 ):
    for x in range( 0 , picWidth ):
      pixel = getPixel( pic, x, y )
      color = getColor( pixel )
      setColor( getPixel( pic, x, picHeight - 1 - y ), color )

   return pic


  
# takes a picture file represented as pic
# and mirros the image from the bottom up

def mirrorYBottomUp( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  for y in range( 0 , picHeight/2 ):
    for x in range( 0 , picWidth ):
      pixel = getPixel( pic, x, y )
      color = getColor( getPixel( pic, x, picHeight - 1 - y ) )
      setColor( pixel, color )

   return pic



# takes a picture file represented as pic
# the function calls mirroX and mirrorY
# to create quad looking effect

def quad( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  pic = mirrorX( pic )
  pic = mirrorY( pic )
      
  return pic      
  

 
  
# takes a picture file represented as pic
# and rotates the pic 90 degrees
# it returns the new pic
      
def rotatePic(pic):
  
  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  newPic = makeEmptyPicture( picHeight, picWidth )
  
  for x in range( 0, picWidth ):
    for y in range( 0, picHeight ):
      pixel = getPixel( pic, x, y )
      color = getColor( pixel );
      setColor( getPixel( newPic, y, picWidth - x - 1 ), color )

  return newPic
 
  

 
   
# Copies one image into the other
# at a specific x and y

def pyCopy(source, target, targetX, targetY):
  
  sourceWidth = getWidth( source )
  sourceHeight = getHeight( source )
  targetWidth = getWidth( target )
  targetHeight = getHeight( target )
  
  for x in range( 0, sourceWidth ):
    for y in range( 0, sourceHeight ):
      pixel = getPixel( source, x, y )
      color = getColor( pixel )
      
      if x + targetX < targetWidth - 1 and y + targetY < targetHeight - 1:      
        setColor( getPixel( target, x + targetX, y + targetY ), color )
        
  return target
        


def makeCollage(pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8):     
  
  collage = makeEmptyPicture( 800, 1000 )
  collage = pyCopy(pic1, collage, 0, 0)
  collage = pyCopy(pic2, collage, 383, 150)
  collage = pyCopy(pic3, collage, 62, 380)
  collage = pyCopy(pic4, collage, 316, 640)
  collage = pyCopy(pic5, collage, 0, 765)
  collage = pyCopy(pic6, collage, 0, 150)
  collage = pyCopy(pic7, collage, 538, 445)
  collage = pyCopy(pic8, collage, 0, 571)
  
  return collage
  
  
pic1 = mirrorY( makePicture('/Users/Captain/Desktop/class-images/group-photo.jpg') )
pic2 = quad( makePicture('/Users/Captain/Desktop/class-images/otter-photo-credit-anitab0000-free-imagaes.jpg') )
pic3 = quad( makePicture('/Users/Captain/Desktop/class-images/python-heart-for-h.jpg') )
pic4 = halfBetter( makePicture('/Users/Captain/Desktop/class-images/python-nails-for-n.jpg') )
pic5 = mirrorX( makePicture('/Users/Captain/Desktop/class-images/python-octopus-for-o.jpg') )
pic6 = makePicture('/Users/Captain/Desktop/class-images/python-pumpkin-for-p.jpg')
pic7 = mirrorYBottomUp( makePicture('/Users/Captain/Desktop/class-images/python-yamaha-for-y.jpg') )
pic8 = mirrorX( makePicture('/Users/Captain/Desktop/class-images/cal-state-campus-shot.jpg') )

newCollage = makeCollage(pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8)
writePictureTo(newCollage, "/Users/Captain/Desktop/class-images/lab-submission/collage.jpg")