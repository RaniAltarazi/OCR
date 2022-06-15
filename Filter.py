import glob
import pathlib
import time
import os
import shutil
import zipfile
from typing import Collection
from PIL import Image
"""""
w = 97
char = chr(w)
os.getcwd()
x = 2
y=0
collection =str(char) 
name = "/"+char+"_"

director = os.path.join(os.getcwd(),collection)
collection1 = collection+ " - -p-"+ str(x)
collection2 = collection + " - NA"

while(w<=122):
  x = 2
  y=0
  collection = str(char)
  name = "/"+char+"_"

  director = os.path.join(os.getcwd(),collection)
  collection1 = collection+ " - -p-"+ str(x)
  collection2 = collection + " - NA"
  try:
    with zipfile.ZipFile(os.path.join(os.getcwd(), collection2+".zip"), 'r') as zip_ref:
      print("Extracted " + collection2 )
      zip_ref.extractall(os.path.join(os.getcwd(),collection2))
  except:
    print("error")
  try:
    os.remove(os.path.join(os.getcwd(),collection2+".zip"))
  except OSError as e:
    print ("Failed with:", e.strerror)# look what it says


  for k in range (7):
    collection1 = collection+ " - -p-"+ str(x)
    try:
      with zipfile.ZipFile(os.path.join(os.getcwd(), collection1+".zip"), 'r') as zip_ref:
        print("Extracted " + collection1 )
        zip_ref.extractall((os.path.join(os.getcwd(),collection1)))
    except:
      print("error")
  
    try:
      os.remove(os.path.join(os.getcwd(),collection1+".zip"))
    except OSError as e:
      print ("Failed with:", e.strerror)# look what it says
    x+=1

  x=2
  y=0
  try:
    os.mkdir(director)
  except OSError as error:
    print(error)
  for i, filename in enumerate(os.listdir(collection2)):
    if (".png" in os.path.splitext(filename) and "websymbols" not in os.path.splitext(filename) and "saturday-night" not in os.path.splitext(filename) and "ge-body" not in os.path.splitext(filename) and "mchandwriting" not in os.path.splitext(filename)and"stand" not in os.path.splitext(filename) and "anglo-saxon-caps" not in os.path.splitext(filename) and "myanmar" not in os.path.splitext(filename) and "living-dead-girl" not in os.path.splitext(filename) and "kansas-city-gothic-caps" not in os.path.splitext(filename) and "judges-sc" not in os.path.splitext(filename)  and "mercutio-nbp-basic" not in os.path.splitext(filename)):
      print(filename)
      os.rename(collection2 + "/" + filename, collection + name + str(y) + ".png")
      y+=1
      time.sleep(0.05)
    
  try:
    shutil.rmtree(os.path.join(os.getcwd(),collection2),ignore_errors=True)
  except OSError as e:
    print ("Failed with:", e.strerror)# look what it says
  for k in range (7):
    collection1 = collection+ " - -p-"+ str(x)
    for i, filename in enumerate(os.listdir(collection1)):
      if (".png" in os.path.splitext(filename) and "websymbols" not in os.path.splitext(filename) and "saturday-night" not in os.path.splitext(filename) and "ge-body" not in os.path.splitext(filename) and "mchandwriting" not in os.path.splitext(filename)and"stand" not in os.path.splitext(filename) and "anglo-saxon-caps" not in os.path.splitext(filename) and "myanmar" not in os.path.splitext(filename) and "living-dead-girl" not in os.path.splitext(filename) and "kansas-city-gothic-caps" not in os.path.splitext(filename) and "judges-sc" not in os.path.splitext(filename)  and "mercutio-nbp-basic" not in os.path.splitext(filename) ):
        print(filename)
        os.rename(collection1 + "/" + filename, collection + name + str(y) + ".png")
        y+=1
        time.sleep(0.05)
    try:
      shutil.rmtree(os.path.join(os.getcwd(),collection1),ignore_errors=True)
    except OSError as e:
      print ("Failed with:", e.strerror)# look what it says
    x+=1
  w+=1
  print(w)
  char = chr(w)
  """
i = 65
while (i<=90):
  for k in range(105):
    try:
      path = (os.getcwd()+"/Letters/"+(str(chr(i))+"/"+str(chr(i))+"_"+str(k)+".png"))
      path2 = (os.getcwd()+"/Letters/"+(str(chr(i))+"/"+str(chr(i))+"_"+str(k)+".jpg"))
      image = Image.open(path)
      image2 = Image.new("RGB",image.size,(255,255,255))
      image2.paste(image, image)
      image2.save(path2)
    except:
      print("error with "+ str(chr(i))+"_"+str(k))
    try:
      os.remove(path)
    except OSError as e:
     print ("Failed with:", e.strerror)# look what it says

  i+=1

i= 97
while(i<=122):
  for k in range (97):
    try:
      path = (os.getcwd()+"/Letters/Lower_"+(str(chr(i))+"/"+str(chr(i))+"_"+str(k)+".png"))
      path2 = (os.getcwd()+"/Letters/Lower_"+(str(chr(i))+"/"+str(chr(i))+"_"+str(k)+".jpg"))
      image = Image.open(path)
      image2 = Image.new("RGB",image.size,(255,255,255))
      image2.paste(image, image)
      image2.save(path2)
    except:
      print("error with "+ str(chr(i))+"_"+str(k))
    try:
      os.remove(path)
    except OSError as e:
     print ("Failed with:", e.strerror)# look what it says
  i+=1
  #"""""
