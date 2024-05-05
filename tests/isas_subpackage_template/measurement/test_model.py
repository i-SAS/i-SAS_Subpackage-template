import unittest
from pathlib import Path

import pandas as pd
from isas_base.subpackage.tests import MeasurementTestFactory

from isas_subpackage_template.measurement import MeasurementTemplate

TEST_PARAMS = {
    'TASK': 'measurement',
    'MODEL_NAME': 'MeasurementTemplate',
    'INSTANCE_NAME': 'template',
    'INPUT_DATA_NAMES': ['rosette_strain_x'],
    'OUTPUT_DATA_NAMES': ['sim_rosette_strain_x'],
    'SENSOR_NAME': 'rosette',
    'STRUCTURAL_MODEL_NAME': None,
    'PARAMS': {'TEST_KEY_1': {'TEST_KEY_1_2': 1.2}},
    'DATADRIVE': Path('/root/datadrive'),
    'DATA_SYSTEM': 'file',
    }


class BaseMeasurementTest:
    factory = MeasurementTestFactory(
        model_class=MeasurementTemplate,
        test_params=TEST_PARAMS,
        )

    BaseMeasurementTestInit, BaseMeasurementTestSimulation, BaseMeasurementTest = factory()


class TestModelInit(BaseMeasurementTest.BaseMeasurementTestInit):
    pass


class TestModelSimulation(BaseMeasurementTest.BaseMeasurementTestSimulation):
    def _test_set_model(self):
        self.assertEqual(self.model.static_data, self.static_data)
        for attr in ('coord_sys', ):
            self.assertIsInstance(getattr(self.model, attr), dict)
            self.assertEqual(set(getattr(self.model, attr).keys()), set(self.TEST_PARAMS['OUTPUT_DATA_NAMES']))

    def _test_call(self, results):
        self.assertIsInstance(results, dict)
        self.assertEqual(set(results.keys()), set(self.TEST_PARAMS['OUTPUT_DATA_NAMES']))
        for res in results.values():
            self.assertIsInstance(res, pd.DataFrame)


class TestModel(BaseMeasurementTest.BaseMeasurementTest):
    def _test_set_model(self):
        self.assertEqual(self.model.static_data, self.static_data)
        for attr in ('coord_sys', ):
            self.assertIsInstance(getattr(self.model, attr), dict)
            self.assertEqual(set(getattr(self.model, attr).keys()), set(self.TEST_PARAMS['OUTPUT_DATA_NAMES']))

    def _test_call(self, results):
        self.assertIsInstance(results, dict)
        self.assertEqual(set(results.keys()), set(self.TEST_PARAMS['OUTPUT_DATA_NAMES']))
        for res in results.values():
            self.assertIsInstance(res, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
