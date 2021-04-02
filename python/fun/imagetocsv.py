from PIL import Image
import numpy as np
import csv

img = np.array(Image.open("pythonworks/fun/images/image.jpeg"))

def createCSV(filename, nparray):
    example = nparray.tolist()
    with open(filename + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(example)

createCSV("funimage", img)