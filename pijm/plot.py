""" Plotting methods
"""


import matplotlib.pyplot as plt
import numpy as np

from pijm.events import StackScroller


# TODO: return type?
# TODO: type hint for array shape?
def plot_zstack(image_array: np.ndarray):
    """Interactively plot stack, capturing scrolling events to scroll through slices

    Args:
       image_array - (n_x, n_y, n_z)
    """
    assert image_array.ndim == 3

    axes_image = plt.imshow(
        image_array[:, :, image_array.shape[2] // 2],
        vmin=image_array.min(),
        vmax=image_array.max(),
    )

    handlers = []

    handlers.append(StackScroller(image_array, axes_image))

    # NOTE: handlers will be garbage collected if not returned
    # TODO: find more elegant solution
    return axes_image, handlers
