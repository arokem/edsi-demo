import numpy as np

def area(radius):
    """Calculate the area of a circle.

    Parameters
    ----------
    radius : float
        The radius of a circle.

    Returns
    -------
    area : float
    """
    return np.pi * (radius ** 2)
