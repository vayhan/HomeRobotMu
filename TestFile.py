import os
if os.path.exists("myvoice.mp3"):
  try:
    os.close("myvoice.mp3")
    os.remove("myvoice.mp3")
  except OSError as e:
    print ("Error: %s - %s." % (e.filename,e.strerror)) 
else:
  print("The file does not exist")
    
