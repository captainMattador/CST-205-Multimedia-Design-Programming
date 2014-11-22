

def getFile():
  return makeSound( pickAFile() )
  
  
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
    
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * .5)
    
    
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
    
    
def maxSample(sound):
  loudestValue = 0
  for sample in getSamples(sound):
    loudestValue = max(getSampleValue(sample), loudestValue)
  return loudestValue
  
  
def maxVolume(sound):
  factor = 32767/maxSample(sound)
  print factor
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  

def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
    
    