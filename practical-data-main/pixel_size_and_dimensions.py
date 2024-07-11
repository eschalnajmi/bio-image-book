from bioimgfunctions import *
from helpers import *

path = find_image('practical-data-main/images/lost_dimensions.tif')[0] 
im_iio = iio.imread(path) # read the px vals
metadata = iio.immeta(path) # get the metadata
print(metadata) # outputs all metadata

# excludes LUT's in metadata
for key, value in metadata.items():
    if not 'LUTs' in key:
        print(f"{key}: {value}")
    
# properties is a curated set of standardised metadata
properties = iio.improps(path, extension=".tif")
print(properties) # can be inaccurate and is therefore not the best to use when px size is important

im_aics = get_px_size_and_metadata('practical-data-main/images/lost_dimensions.tif') 

# check both libraries return same values
print(f'Mean pixel value from imageio:      {im_iio.mean():.2f} (total pixel count {im_iio.size})')
print(f'Mean pixel value from AICSImageIO:  {im_aics.data.mean():.2f} (total pixel count {im_aics.data.size})')

print(f"size of imageio image: {im_iio.shape}")
print(f"size of AICS image: {im_aics.shape}")
print(f"are the arrays equivalent?: {np.array_equal(im_iio, im_aics)}") # checks if the images are equal
# images are not equal since AICS adds some extra 'singleton' dimensions we can remove by squeezing the array
im_aics_squeezed = np.squeeze(im_aics.get_image_data()) # need to get image data to prevent using too much memory
print(f"size of squeezed AICS image: {im_aics_squeezed.shape}")
print(f"are the arrays equivalent after squeezing?: {np.array_equal(im_iio, im_aics_squeezed)}") # checks if the images are equal

# Loop through the first dimension and show images for each plane
n_slices = im_iio.shape[0]
plt.figure(figsize=(12, 4))
for ii in range(n_slices):
    plt.subplot(1, n_slices, ii+1)
    plt.title(f'Plane {ii+1}')
    show_image(im_iio[ii], clip_percentile=1)

