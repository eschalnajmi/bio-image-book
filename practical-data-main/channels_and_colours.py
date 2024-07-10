from bioimgfunctions import *
from helpers import *

im = imread('practical-data-main/images/Neuron-RGB.tif')
changeLUT(im)

rgb_to_single_channel(im, method='split') # split the image into its RGB channels
avg = rgb_to_single_channel(im, method='avg') # average the RGB channels
weightedavg = rgb_to_single_channel(im, method='weightedavg') # calculate weighted avg of RGB channels

changeLUT(avg-weightedavg) # subtract the weighted average from the average to show if images are different, rgb2gray will have rescaled image
changeLUT(avg/255.0 - weightedavg) # makes images comparable without rescaling.

im = load_image('practical-data-main/images/Neuron-RGB.tif', volume=True) # treats the image as a volume
first_channel = im.copy() # copy the image
last_channel = np.moveaxis(im, 0, -1) # move the first axis to the last axis
print(f'First channel shape: {first_channel.shape}, Last channel shape: {last_channel.shape}')

createcomposite(im) # create a composite image of the last channel
