from bioimgfunctions import *

im = imread('practical-data-main/images/Spooked.tif')

print(im.dtype) # output the data type of the array
printsummarystats(im)
genhistogram(im, bins=100)

im_float = im.astype(np.float32) # convert image to float32
printsummarystats(im_float)
genhistogram(im_float, bins=100)

print(np.all(im == im_float)) # output if the image values are identical
# mean values are different but very slightly. This is a precision error.
print(np.allclose(im.mean(), im_float.mean())) # output if the image mean values are identical or close enough

im_u8 = im_float.astype(np.uint8) # convert image to uint8
# by default, numpy will not clip or rescale at all.
printsummarystats(im_u8)
genhistogram(im_u8, bins=100)

array_1 = np.arange(0, 1001, 100) # create an array of values from 0 to 1000 in steps of 100
array_2 = array_1.astype(np.uint8) 
print(np.vstack([array_1, array_2])) # output the two arrays vertically stacked to compare values.

plt.plot(array_1, array_2)
plt.xlabel("original values")
plt.ylabel("uint8 values")
plt.show()

im_u8_clipped = np.clip(im, 0, 255).astype(np.uint8) # clip image values to 0-255 and convert to uint8
printsummarystats(im_u8_clipped)
genhistogram(im_u8_clipped)

temp = im - im.min()
temp /= temp.max()
temp *= 255
im_u8_rescaled = temp.astype(np.uint8) # rescale image values to 0-255, changes pixel values
printsummarystats(im_u8_rescaled)
genhistogram(im_u8_rescaled)
