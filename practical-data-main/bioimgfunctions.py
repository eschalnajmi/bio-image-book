import matplotlib.pyplot as plt
from imageio import imread
import numpy as np
from skimage.color import rgb2gray # rescales images during conversion
from helpers import *

def changeLUT(im_, cmap='gray', title=None, axis=False, vmin=None, vmax=None):
    """
    Function to plot an image with a specified colormap, title, axis, and brightness and contrast.
    :param im_: image to plot
    :param cmap: colormap to use - defaults to gray
    :param title: title of the plot - defaults to None
    :param axis: whether to turn off axis - defaults to False
    :param vmin: minimum pixel value corresponding to the first colour in the colourmap - defaults to None
    :param vmax: maximum pixel value corresponding to the last colour in the colourmap - defaults to None
    :param volume: whether to plot a volume - defaults to False
    """
    if vmin is not None and vmax is not None:
        plt.imshow(im_, cmap=cmap, vmin=vmin, vmax=vmax) # plot image with grayscale colormap
    elif vmin is not None:
        plt.imshow(im_, cmap=cmap, vmin=vmin) # plot image with colormap and modified brightness and contrast
    elif vmax is not None:
        plt.imshow(im_, cmap=cmap, vmax=vmax) # plot image with colormap and modified brightness and contrast
    else:
        plt.imshow(im_, cmap=cmap)

    plt.axis(axis) # decide whether to turn off axis

    if title is not None:
        plt.title(title) # add title
        
    plt.show()

def genhistogram(im_, title=None, bins=None, color=None):
    """
    Generate histogram of pixel values by flattening array into a single 1D list of values
    :param im_: numpy array of pixel values
    :param title: title of histogram
    :param bins: number of bins
    :param color: color of histogram
    """
    flattened = im_.flatten()
    if bins is not None and color is not None:
        plt.hist(flattened, bins=bins, color=color)
    elif bins is not None:
        plt.hist(flattened, bins=bins)
    elif color is not None:
        plt.hist(flattened, color=color)
    else:
        plt.hist(flattened)
    if title is not None:
        plt.title(title)

    plt.show()

def printsummarystats(im_):
    """
    Output mean, min, max, and standard deviation of pixel values
    :param im_: numpy array of pixel values
    """
    print(f"mean: {im_.mean():.3f}, min: {im_.min()}, max: {im_.max()}, std: {im_.std()}") # calculate summary stats
    
def rgb_to_single_channel(im_, method):
    """
    Convert RGB image to single channel image using specified method
    :param im_: numpy array of pixel values
    :param method: method to convert RGB image to single
    """
    if method == "split":
        rgb_split_channels(im_)
    elif method == "avg":
        changeLUT(im_.mean(axis=-1)) # average along the last dimension
        return im_.mean(axis=-1)
    elif method=="weightedavg":
        changeLUT(rgb2gray(im_)) # weighted mean of RGB vals. 0.2125R + 0.7154G + 0.0721B.
        return rgb2gray(im_)

def rgb_split_channels(im_):
    """
    Split RGB image into its 3 channels and plot them
    :param im_: numpy array of pixel values
    """
    plt.figure(figsize=(12,4)) # make wider figure to fit in subplots

    for i in range(3): # show each of 3 channels
        plt.subplot(1, 3, i+1)

        channel = im_[...,i]
        plt.imshow(channel, cmap='gray')
        plt.title(f'Channel {i}')
        plt.axis(False)

    plt.show()

def colorize(im, color, clip_percentile=0.1):
    """
    Helper function to create an RGB image from a single-channel image using a 
    specific color.
    """
    # Check that we do just have a 2D image
    if im.ndim > 2 and im.shape[2] != 1:
        raise ValueError('This function expects a single-channel image!')
        
    # Rescale the image according to how we want to display it
    im_scaled = im.astype(np.float32) - np.percentile(im, clip_percentile)
    im_scaled = im_scaled / np.percentile(im_scaled, 100 - clip_percentile)
    im_scaled = np.clip(im_scaled, 0, 1)
    
    # Need to make sure we have a channels dimension for the multiplication to work
    im_scaled = np.atleast_3d(im_scaled)
    
    # Reshape the color (here, we assume channels last)
    color = np.asarray(color).reshape((1, 1, -1))
    return im_scaled * color

def createcomposite(im_):
    """
    Creates a composite image by adding RGB channels together
    :param im_: numpy array of pixel values
    """
    red = colorize(im_[...,0], (1,0,1))
    changeLUT(red, title="magenta")

    green = colorize(im_[...,2], (0,1,0))
    changeLUT(green, title="green")

    composite = np.clip(red + green, 0, 1)
    changeLUT(composite, title="composite")    