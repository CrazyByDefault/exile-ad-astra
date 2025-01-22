import os
import sys
import cv2 as cv
import numpy as np

from pathlib import Path
from utils.path import get_image_paths_from_folder
from src.gemini_cont import extract_overlay

def contours_to_svg(contours, output_file="contours.svg", shape=None):
  if shape is None:
    print("Please provide a shape (width, height) for the SVG output.")
    sys.exit(-1)
  c = max(contours, key=cv.contourArea) #max contour
  f = open(output_file, 'w+')
  f.write('<svg width="'+str(shape[1])+'" height="'+str(shape[0])+'" xmlns="http://www.w3.org/2000/svg">')
  f.write('<path d="M')

  for i in range(len(c)):
      #print(c[i][0])
      x, y = c[i][0]
      f.write(str(x)+  ' ' + str(y)+' ')

  f.write('"/>')
  f.write('</svg>')
  f.close()

def get_contours(img=None, filename=None, output_file="test-contours.png", io=True, outputOverlays=False):
  if io:
    if filename is None:
      print("Please provide an image filename.")
      sys.exit(-1)
    image = extract_overlay(filename)
  else:
    image = img

  imghsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  lower_blue = np.array([110,35,100])
  upper_blue = np.array([130,140,255])
  mask_blue = cv.inRange(imghsv, lower_blue, upper_blue)
  cv.imwrite("mask-file.png", mask_blue)
  
  blank = np.zeros(image.shape, dtype="uint8")

  contours, hierarchy = cv.findContours(mask_blue, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
  cv.drawContours(blank, contours, -1, (255,140,140), 1)

  # attempt to remove noisy contours
  cntAreas = []
  cntLengths = []
  for i, cnt in enumerate(contours):
    if hierarchy[0][i][3] != -1: # basically look for holes
      # if the size of the contour is less than a threshold (noise)
      cntAreas.append(cv.contourArea(cnt))
      cntLengths.append(cv.arcLength(cnt, True))
      if cv.contourArea(cnt) < 20:
        # print("found hole in contour, filling")
        # Fill the holes in the original image
        cv.drawContours(blank, [cnt], -1, (0,0,255), 1)
      if cv.arcLength(cnt, True) < 20:
        cv.drawContours(blank, [cnt], 0, (0,255,0), 1)
  print("smallest areas", sorted(cntAreas[:20]))
  print("smallest lens", sorted(cntLengths[:20]))


  # dilate the img
  kernelDilate = cv.getStructuringElement(cv.MORPH_ELLIPSE,(6,6))
  dilated = cv.dilate(mask_blue, kernelDilate)
  cv.imwrite("dilated-mask.png", dilated)

  if io:
    cv.imwrite(output_file, blank)

    if outputOverlays:
      im = np.copy(image)
      cv.drawContours(im, contours, -1, (0, 255, 0), 1)
      # generate path with -overlay appended to output_file
      overlayOutputPath = f"{os.path.splitext(output_file)}-overlay.png"
      cv.imwrite(overlayOutputPath, im)
  else:
    return blank, contours

def process_contours_for_folder(inputFolder, outputFolder):
  image_paths = get_image_paths_from_folder(inputFolder)
  
  destinationPaths = []
  for i in range(len(image_paths)):
    print(f"Processing image {i+1}/{len(image_paths)}...")
    outputPath = os.path.join(outputFolder, os.path.basename(image_paths[i]))
    get_contours(filename=image_paths[i], output_file=outputPath)

if __name__ == '__main__':
  filePath = '/home/shashank/personal/poe/codex-helper/images/test'
  outPath = '/home/shashank/personal/poe/codex-helper/out/test'
  Path(outPath).mkdir(parents=True, exist_ok=True)
  process_contours_for_folder(filePath, outPath)
  
  # img = cv.imread("/home/shashank/personal/poe/codex-helper/images/test/image-2_01_01.png")
  # _, conts = get_contours(io=False, img=img)
  # contours_to_svg(conts, shape=img.shape)
  # cv.destroyAllWindows()