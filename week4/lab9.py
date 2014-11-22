
  
# helper function to make and pick a sound file.
def getFile():
  return makeSound( pickAFile() )
  
  
  
# takes s sound clip as source, and a starting point and end point
# then returns the portion clipped out of the source at those
# two points
def clip(source, start, end):
  newClip = makeEmptySound( end - start, 44100)
  index = 0
  for i in range(start, end):
    setSampleValueAt( newClip, index, getSampleValueAt( source, i ))
    index += 1
  return newClip
  
  
# takes a 2 clips as a parameter and a starting value
# the function then copies the source clip into the
# target clip at the start value
def copy(source, target, start):
  for i in range(0, getLength(source)):
    setSampleValueAt( target, start, getSampleValueAt( source, i ))
    start += 1
    

# takes a sound clip as a paramater and retruns a new clip
# that is the reverse of the origianl 
def reverse(sound):
  reversedClip = makeEmptySound( getLength(sound), 44100)
  for i in range(0, getLength(sound)):
    setSampleValueAt( reversedClip, getLength(sound) - i - 1, getSampleValueAt( sound, i ))
  return reversedClip

  

# this fucntion makes a new sound from 5 diff clips
# it relies on the fucntions clip and copy to combine
# the files accordingly 
def makeNewSound():
  clip1 = makeSound("/Users/Captain/GitHub/audio-files/showedpictures.wav")
  clip1 = clip(clip1, 1011, 72792)
  clip1Length = getLength(clip1) + int(0.2 * getSamplingRate(clip1)) 
  
  clip2 = makeSound("/Users/Captain/GitHub/audio-files/peopleandfruit.wav")
  clip2 = clip(clip2, 200060, 254362)
  clip2Length = getLength(clip2)
 
  clip3 = makeSound("/Users/Captain/GitHub/audio-files/blowup.wav")
  clip3Length = getLength(clip3) + int(0.2 * getSamplingRate(clip3))

  clip4 = makeSound("/Users/Captain/GitHub/audio-files/disgusting.wav")
  clip4 = clip(clip4, 2616, 78480)
  clip4Length = getLength(clip4) + int(0.2 * getSamplingRate(clip4))
  
  clip5 = makeSound("/Users/Captain/GitHub/audio-files/salmon.wav")
  clip5 = clip(clip5, 1408, 86944)
  clip5Length = getLength(clip5)
  
  newClip = makeEmptySound( clip1Length + clip2Length + clip3Length + clip4Length + clip5Length, 44100)
  
  copy(clip1, newClip, 0)
  copy(clip2, newClip, clip1Length)
  copy(clip3, newClip, clip1Length + clip2Length)
  copy(clip4, newClip, clip1Length + clip2Length + clip3Length)
  copy(clip5, newClip, clip1Length + clip2Length + clip3Length + clip4Length)
  writeSoundTo( newClip, "/Users/Captain/GitHub/audio-files/new-sound.wav")
  
  
  