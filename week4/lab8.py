

# Matthew Bozelka - Lab Number 8
# Peer Partners - Julia Diliberto, Robert Contreras, Ryan Doherty


# helper function to make and pick a sound file.
def getFile():
  return makeSound( pickAFile() )
  

# takes sound as a parameter
# and Increases the volume of the sound
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)



# takes sound as a parameter
# and Decreases the volume of the sound 
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * .5)
    

 
# takes sound as a parameter and a number representing a factor
# and multiplies each sample by that factor
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
    


# takes sound as a parameter
# and returns the loudest samples value   
def maxSample(sound):
  loudestValue = 0
  for sample in getSamples(sound):
    loudestValue = max(getSampleValue(sample), loudestValue)
  return loudestValue
  

 
# takes sound as a parameter
# and maxes all the samples
# based on the loudest sample 
def maxVolume(sound):
  factor = 32767/maxSample(sound)
  print factor
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)



# takes sound as a parameter
# and normalizes the sound
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
    
    