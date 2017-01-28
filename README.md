# marker-crop

A set of tools for rotating, cropping, and binding the images from a
scanned book into a PDF.

## crop.py

Usage: `python crop.py <infile> <outfile>`

crop.py will take an input image, search for markers on that image,
then rotate it (increments of 90 degrees only) and crop it using the
orientation and borders of the markers.

## bind.py

Usage: `python bind.py <path>`

bind.py processes an entire folder of images, running crop.py on each
one. Afterwards, all the images are bound together into a single PDF
file. These are put into the 'cropped' and 'bound' subfolders
respectively.

The images in the directory should be in the form of a four-digit
number followed by '.jpg'. Example: `0004.jpg`

## Dependencies

These files depend on opencv3, the aruco module in opencv3-contrib, and img2pdf

