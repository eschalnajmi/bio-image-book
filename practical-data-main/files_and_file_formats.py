from bioimgfunctions import *
import tifffile

# Pillow is a fork of the Python Imaging Library (PIL) which can rw imgs as well as draw on them.
# Pillow does not work on NumPy Arrays.
#read_nparray_with_pillow('practical-data-main/images/happy_cell.tif')

# read the image using imageio
path = find_image('practical-data-main/images/happy_cell.tif')[0]
im = imread(path)
print(f"mean: {im.mean()}")

# read the image using tifffile, a package useful for rw tiff files
im = tifffile.imread(path)
print(f"mean: {im.mean()}")