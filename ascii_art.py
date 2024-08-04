import cv2
image = cv2.imread('./images.png',cv2.IMREAD_GRAYSCALE)
import math
import sys


def readIMG(filename):
    return cv2.imread(filename,cv2.IMREAD_GRAYSCALE)


def convertToAscii(input):
    brightness_string = ["#","W","o","-"]
    (h, w) = image.shape[:2]
    new_width = 50
    aspect_ratio = h / w
    new_height = int(new_width * aspect_ratio)
    resized_image = cv2.resize(image, (new_width, new_height))

    art_ascii = []
    print("image shape is : ",resized_image.shape)

    for i in range(len(resized_image)):
        art_row = []
        for item in resized_image[i]:
            art_row.append(brightness_string[math.floor(item*(len(brightness_string)/256))])
        
        art_ascii.append(art_row)

    return art_ascii


def printASCII(input):
    for item in input:
        for element in item:
            print(element+"",end='')
        print("")



args = sys.argv

try:
    printASCII(convertToAscii(readIMG(args[1])))


except:
    print("Error!! Image path is not provided")



