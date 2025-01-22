import cv2 as cv

import numpy as np
import sys
import os

from islotate_map import sobel
from contours import get_contours

lower_blue = np.array([110,35,100])
upper_blue = np.array([130,140,255])

def get_image_paths_from_folder(folder):
  # get all image file paths in folder
  img_paths = []
  for root, _, files in os.walk(folder):
    for file in files:
      if file.endswith(('.png', '.jpg', '.jpeg')):
        img_paths.append(os.path.join(root, file))
  print(img_paths)
  return img_paths

def stitch_images_in_folder(folder=None, output_file="test.png"):
  # read input images
  if folder is None:
    print("Please provide a folder path.")
    sys.exit(-1)

  # check if the folder exists
  if not os.path.exists(folder):
    print("Folder path does not exist.")
    sys.exit(-1)
  
  img_names = get_image_paths_from_folder(folder)

  # if len(img_names) <= 2:
  #   import image_slicer
  #   for img_name in img_names:
  #     image_slicer.slice(img_name, 4)
  #     os.remove(img_name)
  #   print("Image cutting completed successfully.")
  #   img_names = get_image_paths_from_folder(folder)

  imgs = []
  img_masks = []
  for img_name in img_names:
    img = cv.imread(img_name)
    if img is None:
      print("can't read image " + img_name)
      sys.exit(-1)
    blank, _ = get_contours(img=img, io=False)
    imgs.append(blank)

    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask_blue = cv.inRange(imghsv, lower_blue, upper_blue)
    img_masks.append(mask_blue)


  stitcher = cv.Stitcher.create(cv.Stitcher_SCANS)
  status, stitchResult = stitcher.stitch(imgs)

  if status != cv.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)

  cv.imwrite(output_file, stitchResult)
  print("stitching completed successfully. %s saved!" % output_file)

def manual_affine_stitch(folder=None, output_file="test.png"):
  # read input images
  if folder is None:
    print("Please provide a folder path.")
    sys.exit(-1)

  # check if the folder exists
  if not os.path.exists(folder):
    print("Folder path does not exist.")
    sys.exit(-1)
  
  img_names = get_image_paths_from_folder(folder)

  # if len(img_names) <= 2:
  #   import image_slicer
  #   for img_name in img_names:
  #     image_slicer.slice(img_name, 4)
  #     os.remove(img_name)
  #   print("Image cutting completed successfully.")
  #   img_names = get_image_paths_from_folder(folder)

  imgs = []
  img_masks = []
  for img_name in img_names:
    img = cv.imread(img_name)
    if img is None:
      print("can't read image " + img_name)
      sys.exit(-1)
    contourImg, _ = get_contours(io=False, img=img)
    imgs.append(contourImg)

    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask_blue = cv.inRange(imghsv, lower_blue, upper_blue)
    img_masks.append(mask_blue)
  
  sift = cv.SIFT_create()
  keypoints = []
  for img in imgs:
    kp, des = sift.detectAndCompute(img, None)
    keypoints.append(kp)
    kpImg = img.copy()
    kpImg = cv.drawKeypoints(image=img, keypoints=kp, outImage=kpImg, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imwrite("testimg.png", kpImg)
    
    
  affineMatcher = cv.detail.AffineBestOf2NearestMatcher(full_affine=True, try_use_gpu=False)

if __name__ == '__main__':
  stitch_images_in_folder("/home/shashank/personal/poe/codex-helper/images/bog")
  # manual_affine_stitch("/home/shashank/personal/poe/codex-helper/images/bog")
  cv.destroyAllWindows()
