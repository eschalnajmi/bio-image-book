import matplotlib.pyplot as plt
from imageio import imread

def changeLUT(im_, cmap='gray', title=None, axis=False, vmin=None, vmax=None):
    """
    Function to plot an image with a specified colormap, title, axis, and brightness and contrast.
    :param im_: image to plot
    :param cmap: colormap to use - defaults to gray
    :param title: title of the plot - defaults to None
    :param axis: whether to turn off axis - defaults to False
    :param vmin: minimum pixel value corresponding to the first colour in the colourmap - defaults to None
    :param vmax: maximum pixel value corresponding to the last colour in the colourmap - defaults to None
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

im_ = imread('practical-data-main/images/Spooked.tif') # read the image
plt.imshow(im_) # plot image with default colormap
plt.show() # show the plot

# cmap argument to change the colourmap of the image.
# vmin argument to change the minimum pixel value corresponding to the first colour in the colourmap.
# vmax argument to change the maximum pixel value corresponding to the last colour in the colourmap.

changeLUT(im_)  # plot image with grayscale colormap
changeLUT(im_, cmap='gray_r') # plot image with grayscale reverse colormap to create an Xray
changeLUT(im_, vmin=0, vmax=8, title='Spooked', axis=True) # plot image with adjusted brightness and contrast, title, axis

