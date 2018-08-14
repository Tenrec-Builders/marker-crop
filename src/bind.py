import os, sys, re
from crop import crop

# Create the directories in the target path to contain the cropped pages and bound pdf
def makeDirs(root):
  os.system("mkdir -p " + os.path.join(root, "cropped"))
  os.system("mkdir -p " + os.path.join(root, "bound"))

# Return a list of filenames (not full pathnames) of the raw files to
# process in the target path
def findImages(root):
  result = []
  valid = re.compile('^[0-9]+.[jJ][pP][eE]?[gG]$')
  all = os.listdir(root)
  for filename in all:
    path = os.path.join(root, filename)
    if (os.path.isfile(path) and
        valid.match(filename)):
      result.append(filename)
  return result

# Crop each file in the target path
def cropAll(root):
  imageList = findImages(root)
  for image in imageList:
    imageOut = re.sub(r'(.[jJ][pP][eE]?[gG])$', '.jpg', image)
    crop(os.path.join(root, image), os.path.join(root, "cropped", imageOut))

# Bind cropped files into a PDF
def bindAll(root):
  os.system("img2pdf -o " + os.path.join(root, "bound/book.pdf") + " "  + os.path.join(root,  "cropped/*.jpg"))
  
def main():
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: bind.py <path>\n")
    exit(1)
  root = sys.argv[1]
  makeDirs(root)
  cropAll(root)
  bindAll(root)

main()
