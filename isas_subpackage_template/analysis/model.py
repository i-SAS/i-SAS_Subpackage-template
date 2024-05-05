import pandas as pd
from isas_base.data import DynamicData
from isas_base.subpackage import BaseAnalysis


class Model(BaseAnalysis):
    """A template of analysis model class."""
    # Edit following constant values.
    MODEL_NAME = 'AnalysisTemplate'
    DEFAULT_CFG = {
        'TEST_KEY_0': 0,
        'TEST_KEY_1': {
            'TEST_KEY_1_1': 1.1,
            'TEST_KEY_1_2': None,
            },
        }
    DEFAULT_INPUT_DATA_NAME_DICT = {
        'input_quantity': ['input_data_1']
        }
    DEFAULT_OUTPUT_DATA_NAME_DICT = {
        'output_quantity': ['output_data_1']
        }

    def _set_model(self) -> None:
        """Arbitrary process executed in model setting."""
        # Set coordinate system and model compnent type of results.
        # The keys are names of output data name (str), and the values
        # are names of coordinate system or model compnent type.
        # r1, r2, r3, and structural model connection are optional.

        # Example. ---
        self.coord_sys = {
            data_name: 'local'
            for data_name in self.output_data_names
            }
        self.component_name = {
            data_name: 'fe_elem'
            for data_name in self.output_data_names
            }
        self.r1 = {
            data_name: 0
            for data_name in self.output_data_names
            }
        self.r2 = {
            data_name: 0
            for data_name in self.output_data_names
            }
        self.r3 = {
            data_name: 0
            for data_name in self.output_data_names
            }
        # --- The end of example.

        # Set connections between output data and structural model.

        # Example. ---
        for input_data_name, output_data_name in zip(self.input_data_names, self.output_data_names):
            structural_model_name = self.output_data_name_to_structural_model_name[output_data_name]
            structural_model_info = self.static_data.time_series_metadata[
                input_data_name].structural_model_info.get(structural_model_name, None)
            if structural_model_info is not None:
                self.structural_model_connections[output_data_name] = structural_model_info.connection
        # --- The end of example.

        # (Optional) Calculate intermediate data.

        # Example. ---
        pass
        # --- The end of example.

    def __call__(
            self,
            dynamic_data: DynamicData | None = None,
            ) -> dict[str, pd.DataFrame]:
        """Analyze data and return results.

        Args:
            dynamic_data: Dynamic data calculated previously.

        Returns:
            Results of analysis. The keys are names of output data, and the values are results.
        """
        # Example. ---

        # Couner case.
        if dynamic_data is None or any([
                data_name not in dynamic_data.time_series_data
                for data_name in self.input_data_names
                ]):
            results = {data_name: None for data_name in self.output_data_names}
            return results

        # Calculate results.
        results = {
            output_data_name: dynamic_data.time_series_data[input_data_name].fields
            for input_data_name, output_data_name in zip(self.input_data_names, self.output_data_names)
            }

        # --- The end of example.
        return results

    def exit(self):
        """Exit model."""
        pass
