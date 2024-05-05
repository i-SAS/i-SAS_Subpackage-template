import numpy as np
import pandas as pd
from isas_base.data import DynamicData
from isas_base.subpackage import BaseMeasurement


class Model(BaseMeasurement):
    """A template of measurement model class."""
    # Edit following constant values.
    MODEL_NAME = 'MeasurementTemplate'
    INPUT_DATA_NUM = None
    OUTPUT_DATA_NUM = None
    DEFAULT_CFG = {
        'TEST_KEY_0': 0,
        'TEST_KEY_1': {
            'TEST_KEY_1_1': 1.1,
            'TEST_KEY_1_2': None,
            },
        }
    DEFAULT_INPUT_DATA_NAMES = ['input_data_1']
    DEFAULT_OUTPUT_DATA_NAMES = ['output_data_1']

    def _set_model(self) -> None:
        """Arbitrary process executed in model setting."""
        # Set coordinate system of results here.
        # The keys are names of output data, and the values are names of coordinate system.

        # Example. ---
        if self.simulation:
            self.coord_sys = {
                output_data_name: self.static_data.time_series_metadata[input_data_name].coord_sys
                for input_data_name, output_data_name in zip(self.input_data_names, self.output_data_names)
                }
        else:
            self.coord_sys = {
                data_name: 'sensor'
                for data_name in self.output_data_names
                }
        # --- The end of example.

        # Calculate intermediate data here.
        # Example. ---
        pass
        # --- The end of example.

    def __call__(
            self,
            dynamic_data: DynamicData | None = None,
            ) -> dict[str, pd.DataFrame]:
        """Measure data and return results.

        Args:
            dynamic_data: Dynamic data calculated previously.

        Returns:
            Results of measurement. The keys are names of output data, and the values are results.
        """
        # Example. ---

        if self.simulation:
            results = self._simulate(dynamic_data)
        else:
            results = self._measure(dynamic_data)

        # --- The end of example.
        return results

    def _simulate(
            self,
            dynamic_data: DynamicData | None,
            ) -> dict[str, pd.DataFrame]:
        """Simulate measurement data.

        Args:
            dynamic_data: Dynamic data calculated previously.

        Returns:
            Results of measurement. The keys are names of output data, and the values are results.
        """
        # Couner case.
        if dynamic_data is None or any([
                data_name not in dynamic_data.time_series_data
                for data_name in self.input_data_names
                ]):
            results = {data_name: None for data_name in self.output_data_names}
            return results

        # Simulate measurement data.
        results = {
            output_data_name: dynamic_data.time_series_data[input_data_name].fields
            for input_data_name, output_data_name in zip(self.input_data_names, self.output_data_names)
            }
        return results

    def _measure(
            self,
            dynamic_data: DynamicData | None,
            ) -> dict[str, pd.DataFrame]:
        """Measure data.

        Args:
            dynamic_data: Dynamic data calculated previously.

        Returns:
            Results of measurement. The keys are names of output data, and the values are results.
        """
        data_num = 18
        frame_num = 1
        results = {
            data_name: pd.DataFrame(np.empty((frame_num, data_num)))
            for data_name in self.output_data_names
            }
        return results

    def exit(self):
        """Exit model."""
        pass
