import os
import sys

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
