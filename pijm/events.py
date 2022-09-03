""" Event handlers
"""

from abc import ABC, abstractmethod

import numpy as np
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure
from matplotlib.image import AxesImage


class ScrollHandler(ABC):
    def __init__(self, fig: Figure) -> None:
        fig.canvas.mpl_connect("scroll_event", self.on_scroll)

        self.__fig = fig

    @abstractmethod
    def on_scroll(self, event: MouseEvent) -> None:
        pass


class StackScroller(ScrollHandler):
    def __init__(self, image_array: np.ndarray, axes_image: AxesImage) -> None:
        assert image_array.ndim == 3
        assert axes_image.get_array().shape == image_array.shape[:1]

        self.__image_array = image_array
        self.__axes_image = axes_image

        self.__slice_idx = image_array.shape[2] // 2
        self.__title = axes_image.axes.get_title()

        super().__init__(axes_image.get_figure())

    def on_scroll(self, event: MouseEvent) -> None:
        if event.button == "up":
            self.__slice_idx = min(self.__slice_idx + 1, self.__image_array.shape[2])
        else:
            self.__slice_idx = max(self.__slice_idx - 1, 0)

        self.update()

    def update(self):
        self.__axes_image.set_data(self.__image_array[:, :, self.__slice_idx])
        self.__axes_image.axes.set_title(
            f"z:{self.__slice_idx}/{self.__image_array.shape[2]}, {self.__title}"
        )
        self.__axes_image.figure.canvas.draw()
