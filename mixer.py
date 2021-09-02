import PIL
import os

imagePath = "./jigsaw"

for dirs in os.walk(imagePath):
    for dir in dirs:
      print(dir)
