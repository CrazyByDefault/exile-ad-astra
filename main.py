import sys
import os
from pathlib import Path
from src.contours import process_contours_for_folder
from utils.path import get_image_paths_from_folder

inPath = '/home/shashank/personal/poe/codex-helper/images/test'
outPath = '/home/shashank/personal/poe/codex-helper/out/test'

# get inPath and outPath from arguments if available
if len(sys.argv) > 1:
    inPath = sys.argv[1]
if len(sys.argv) > 2:
    outPath = sys.argv[2]

Path(outPath).mkdir(parents=True, exist_ok=True)
process_contours_for_folder(inPath, outPath)