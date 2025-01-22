import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def sobel(img=None, filename=None, output_file="test-sobel.png", io=True):
  if io:
    if filename is None:
      print("Please provide an image filename or image object.")
      sys.exit(-1)
    image = cv.imread(filename)
  else:
    image = img

  # Convert to grayscale
  gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

  # Apply Gaussian smoothing (optional)
  blurred_image = cv.GaussianBlur(gray_image, (3, 3), 0)

  # Sobel operators
  Gx = cv.Sobel(blurred_image, cv.CV_64F, 1, 0, ksize=3)
  Gy = cv.Sobel(blurred_image, cv.CV_64F, 0, 1, ksize=3)

  # Gradient magnitude
  G = np.sqrt(Gx**2 + Gy**2)

  # Normalize to range 0-255
  Gx = np.uint8(255 * np.abs(Gx) / np.max(Gx))
  Gy = np.uint8(255 * np.abs(Gy) / np.max(Gy))
  G = np.uint8(255 * G / np.max(G))

  if io:
    cv.imwrite(output_file, G)
  else:
    return G

if __name__ == '__main__':
  sobel(filename="/home/shashank/personal/poe/codex-helper/images/test/image-1.png")
  cv.destroyAllWindows()