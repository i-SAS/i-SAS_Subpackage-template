import unittest
from pathlib import Path

from isas_base.subpackage.tests import VisualizationTestFactory

from isas_subpackage_template.visualization import Dropdowns

TEST_PARAMS = {
    'MODEL_NAME': 'Dropdowns',
    'SIZE_RATIO': (1, 1),
    'INSTANCE_NAME': 'template',
    'INPUT_DATA_NAMES': [],
    'INPUT_DATA_NAME_DICT': {},
    'OUTPUT_DATA_NAMES': [],
    'OUTPUT_DATA_NAME_DICT': {},
    'SENSOR_NAME': None,
    'STRUCTURAL_MODEL_NAME': None,
    'PARAMS': {'DROPDOWN_LIST': ['dropdown_value_1', 'dropdown_value_2']},
    'VARIABLES': {},
    'DATADRIVE': Path('/root/datadrive'),
    'DATA_SYSTEM': 'file',
    }


class BaseVisualizationTest:
    factory = VisualizationTestFactory(
        model_class=Dropdowns,
        test_params=TEST_PARAMS,
        )

    BaseVisualizationTestInit, BaseVisualizationTest = factory()


class TestModelInit(BaseVisualizationTest.BaseVisualizationTestInit):
    pass


class TestModel(BaseVisualizationTest.BaseVisualizationTest):
    def _test_set_model(self):
        self.assertEqual(self.model.static_data, self.static_data)

    def _test_call(self, results, variables):
        self.assertEqual(len(variables), 1)
        for key, value in variables.items():
            self.assertEqual(key, self.model.cfg['VARIABLE_NAME'])
            self.assertEqual(value, self.model.cfg['DROPDOWN_LIST'][0])


if __name__ == '__main__':
    unittest.main()
