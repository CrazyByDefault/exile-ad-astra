import sys
import os
from pathlib import Path
from src.contours import process_contours_for_folder
from utils.path import get_image_paths_from_folder

filePath = '/home/shashank/personal/poe/codex-helper/images/praetor'
outPath = '/home/shashank/personal/poe/codex-helper/out/test'
Path(outPath).mkdir(parents=True, exist_ok=True)
process_contours_for_folder(filePath, outPath)