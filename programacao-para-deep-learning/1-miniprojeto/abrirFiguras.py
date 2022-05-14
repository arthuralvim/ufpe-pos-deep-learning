import PIL
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image
import numpy as np

def getListOfListImage(imgPath="", showImage=False):
  #urlLena = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
  urlLena = "Lenna.png"
  if (imgPath == ""):
    img = PIL.Image.open(urlLena)
  else:
    img = PIL.Image.open(imgPath)
  
  gray_img = img.convert("L")

  gray_img = gray_img.resize((128,128))

  if  showImage:
    plt.imshow(gray_img, cmap='gray')
  xSize, ySize = gray_img.size

  listaPixels = list(gray_img.getdata())
  arrayPixels = np.array(listaPixels)

  listOfListImage = arrayPixels.reshape((xSize, ySize)).tolist()
  return listOfListImage, np.zeros((xSize,ySize)).tolist()

def getImageFromListofList(listOfListImage):
  newImageArray = np.array(listOfListImage)

  #%matplotlib inline
  imshow(np.asarray(newImageArray),cmap='gray')