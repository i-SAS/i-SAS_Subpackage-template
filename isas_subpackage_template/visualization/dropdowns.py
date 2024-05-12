from typing import Any

from isas_base.data import DynamicData
from isas_base.subpackage import BaseVisualization
from PySide6 import QtWidgets


class Dropdowns(BaseVisualization):
    """A templaten of Visualization model class."""
    # Edit following constant values.
    MODEL_NAME = 'Dropdowns'
    DEFAULT_CFG = {
        'UPDATE_PRIORITY': 0,
        'COLOR_THEME': 'default',  # automatically defined by selected CSS theme
        'DROPDOWN_LIST': None,
        'VARIABLE_NAME': 'dropdown_value',
        }
    DEFAULT_INPUT_DATA_NAME_DICT = {}
    DEFAULT_OUTPUT_DATA_NAME_DICT = {}

    def _create_widget(self) -> QtWidgets.QWidget:
        """Arbitrary process executed in widget creating.

        Returns:
            A widget of Qt.
        """
        # Example. ---
        widget = QtWidgets.QComboBox()
        # --- The end of example.
        return widget

    def _set_model(self) -> None:
        """Arbitrary process executed in model setting."""
        # Example. ---
        self.widget.addItems(self.cfg['DROPDOWN_LIST'])
        self.widget.setStyleSheet(f'color: {self.COLOR_THEME[self.cfg["COLOR_THEME"]]}')
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
        results = {}
        selected_id = self.widget.currentIndex()
        new_variables = {self.cfg['VARIABLE_NAME']: self.cfg['DROPDOWN_LIST'][selected_id]}
        # --- The end of example.
        return results, new_variables

    def exit(self) -> None:
        """Exit model."""
        pass
