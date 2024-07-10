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