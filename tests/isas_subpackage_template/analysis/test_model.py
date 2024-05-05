import unittest
from pathlib import Path

import pandas as pd
from isas_base.subpackage.tests import AnalysisTestFactory

from isas_subpackage_template.analysis import AnalysisTemplate

INPUT_DATA_NAMES = ['rosette_strain_x']
OUTPUT_DATA_NAMES = ['rosette_strain_x_analysed']
TEST_PARAMS = {
    'TASK': 'analysis',
    'MODEL_NAME': 'AnalysisTemplate',
    'INSTANCE_NAME': 'template',
    'INPUT_DATA_NAMES': INPUT_DATA_NAMES,
    'INPUT_DATA_NAME_DICT': {'input_quantity': INPUT_DATA_NAMES},
    'OUTPUT_DATA_NAMES': OUTPUT_DATA_NAMES,
    'OUTPUT_DATA_NAME_DICT': {'output_quantity': OUTPUT_DATA_NAMES},
    'SENSOR_NAME': None,
    'STRUCTURAL_MODEL_NAME': 'beam',
    'PARAMS': {'TEST_KEY_1': {'TEST_KEY_1_2': 1.2}},
    'DATADRIVE': Path('/root/datadrive'),
    'DATA_SYSTEM': 'file',
    }


class BaseAnalysisTest:
    factory = AnalysisTestFactory(
        model_class=AnalysisTemplate,
        test_params=TEST_PARAMS,
        )

    BaseAnalysisTestInit, BaseAnalysisTest = factory()


class TestModelInit(BaseAnalysisTest.BaseAnalysisTestInit):
    pass


class TestModel(BaseAnalysisTest.BaseAnalysisTest):
    def _test_set_model(self):
        self.assertEqual(self.model.static_data, self.static_data)
        for attr in ('coord_sys', 'component_name', 'r1', 'r2', 'r3'):
            self.assertIsInstance(getattr(self.model, attr), dict)
            self.assertEqual(set(getattr(self.model, attr).keys()), set(self.TEST_PARAMS['OUTPUT_DATA_NAMES']))

    def _test_call(self, results):
        for input_data_name, output_data_name in zip(
                self.TEST_PARAMS['INPUT_DATA_NAMES'], self.TEST_PARAMS['OUTPUT_DATA_NAMES']):
            self.assertIsInstance(results[output_data_name], pd.DataFrame)
            pd.testing.assert_frame_equal(
                results[output_data_name],
                self.dynamic_data.time_series_data[input_data_name].fields
                )


if __name__ == '__main__':
    unittest.main()
