#Name: Laura Collins
#V-number:V00763363
#Date: 2026-02-08
# Print Cat
ears = "  /\ /\  "
eyes = "   o o   "
whiskers = "  = =   "
mouth = "   <>    "
#Width is the maximum length of the strings
width = max(len(ears), len(eyes), len(whiskers), len(mouth))
print(ears.center(width))
print(eyes.center(width))
print(whiskers.center(width))
print(mouth.center(width))       

