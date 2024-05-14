from typing import Any

import matplotlib.pyplot as plt
from isas_base.data import DynamicData
from isas_base.subpackage import BaseVisualization
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from PySide6 import QtWidgets


class TextDrawer(BaseVisualization):
    """A templaten of Visualization model class."""
    # Edit following constant values.
    MODEL_NAME = 'TextDrawer'
    DEFAULT_CFG = {
        'UPDATE_PRIORITY': 0,
        'COLOR_THEME': 'default',  # automatically defined by selected CSS theme
        'VARIABLE_NAME': 'drawn_text',
        'FONTSIZE': None,
        }
    DEFAULT_INPUT_DATA_NAME_DICT = {}
    DEFAULT_OUTPUT_DATA_NAME_DICT = {}

    def _create_widget(self) -> QtWidgets.QWidget:
        """"Arbitrary process executed in widget creating.

        Returns:
            A widget of Qt.
        """
        # Example. ---
        fig_size = (1, 1)  # dummy size
        fig = plt.figure(figsize=fig_size)
        fig.patch.set_alpha(0.0)
        widget = FigureCanvas(fig)
        self.ax = widget.figure.subplots()
        # --- The end of example.
        return widget

    def _set_model(self) -> None:
        """Arbitrary process executed in model setting."""
        # Example. ---
        pass
        # --- The end of example.

    def __call__(
            self,
            dynamic_data: DynamicData | None = None,
            variables: dict | None = None,
            ) -> tuple[dict[str, Any]]:
        """Update figure.

        Args:
            dynamic_data: Dynamic data calculated previously.
            variables: Variables for interactive GUI. The keys are names of valiables,
                and the values are data.

        Returns:
            A tuple of followings.
                results: Results of analysis. The keys are names of output data, and the values are results.
                new_variables: New variables for interactive GUI. The keys are names of valiables,
                    and the values are variables.
        """
        # Example. ---
        self.text = variables.get(self.cfg['VARIABLE_NAME'], 'example')
        self.ax.clear()
        self.ax.text(
            0.5,
            0.5,
            self.text,
            horizontalalignment='center',
            verticalalignment='center',
            transform=self.ax.transAxes,
            fontsize=self.cfg['FONTSIZE'],
            color=self.COLOR_THEME[self.cfg['COLOR_THEME']],
            )
        for edge in ('top', 'right'):
            self.ax.spines[edge].set_visible(False)
        self.ax.figure.canvas.draw()

        results = {}
        new_variables = {}
        # --- The end of example.
        return results, new_variables

    def exit(self) -> None:
        """Exit model."""
        pass
