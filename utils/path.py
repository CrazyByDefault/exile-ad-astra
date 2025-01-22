import os

def get_image_paths_from_folder(folder):
  # get all image file paths in folder
  img_paths = []
  for root, _, files in os.walk(folder):
    for file in files:
      if file.endswith(('.png', '.jpg', '.jpeg')):
        img_paths.append(os.path.join(root, file))
  print(img_paths)
  return img_paths