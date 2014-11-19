

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
  



# takes a picture file represented as pic
# the function calls mirroX and mirrorY
# to create quad looking effect

def quad( pic ):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  
  pic = mirrorX( pic )
  pic = mirrorY( pic )


    
# takes a picture file represented as pic
# and makes an exact copy of the pic
# it returns the new pic
            
def simpleCopy(pic):

  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  newPic = makeEmptyPicture( picWidth, picHeight )
  
  for x in range( 0, picWidth ):
    for y in range( 0, picHeight ):
      pixel = getPixel( pic, x, y )
      color = getColor( pixel );
      setColor( getPixel( newPic, x, y ), color )
      
  show( newPic )
  return newPic

 
  
   
# takes a picture file represented as pic
# and rotates the pic 90 degrees
# it returns the new pic
      
def rotatePic(pic):
  
  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  newPic = makeEmptyPicture( picHeight, picWidth )
  
  for x in range( 0, picWidth ):
    for ymy in range( 0, picHeight ):
      pixel = getPixel( pic, x, y )
      color = getColor( pixel );
      setColor( getPixel( newPic, y, picWidth - x - 1 ), color )
      
  show( newPic )
  return newPic
 
  
   
    
# takes a picture file represented as pic
# and shrinks the pic in half by discarding
# every other pixel, it returns the new pic
       
def shrink( pic ):
  
  picWidth = getWidth( pic )
  picHeight = getHeight( pic )
  newPic = makeEmptyPicture( picWidth/2, picHeight/2 )
  newWidth = getWidth( newPic )
  newHeight = getHeight( newPic )
  newX = 0
  newY = 0
  
  for x in range( 0, picWidth, 2 ):
    for y in range ( 0, picHeight, 2 ):
      
      if x/2 <= newWidth - 1 and y/2 <= newHeight - 1:
        pixel = getPixel( pic, x, y )
        color = getColor( pixel );
        setColor( getPixel( newPic, newX, newY ), color )
        newY = newY + 1
        
    newX = newX + 1
    newY = 0
  
  return newPic
        
        
        
