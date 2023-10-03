from skimage import feature
import numpy as np


class LocalBinaryPatterns:

    def __init__(self, numPoints, radius):
        """store the number of points and radius"""
        self.numPoints = numPoints
        self.radius = radius

    def describe(self, image, method="nri_uniform"):
        """ compute the Local Binary Pattern representation
            of the image, and then use the LBP representation
            to build the histogram of patterns
        """
        lbp = feature.local_binary_pattern(image, self.numPoints,
                                           self.radius, method)

        hist = np.unique(lbp, return_counts=True)
        # normalize the histogram
        hist = hist[1].astype("float")
        hist /= (hist.sum())

        # return the histogram of Local Binary Patterns
        return hist
