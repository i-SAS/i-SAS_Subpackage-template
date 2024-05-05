import unittest
from pathlib import Path

from isas_base.subpackage.tests import VisualizationTestFactory

from isas_subpackage_template.visualization import TextDrawer

TEST_PARAMS = {
    'MODEL_NAME': 'TextDrawer',
    'SIZE_RATIO': (1, 1),
    'INSTANCE_NAME': 'template',
    'INPUT_DATA_NAMES': [],
    'INPUT_DATA_NAME_DICT': {},
    'OUTPUT_DATA_NAMES': [],
    'OUTPUT_DATA_NAME_DICT': {},
    'SENSOR_NAME': None,
    'STRUCTURAL_MODEL_NAME': None,
    'PARAMS': {'FONTSIZE': 10},
    'VARIABLES': {'drawn_text': 'test'},
    'DATADRIVE': Path('/root/datadrive'),
    'DATA_SYSTEM': 'file',
    }


class BaseVisualizationTest:
    factory = VisualizationTestFactory(
        model_class=TextDrawer,
        test_params=TEST_PARAMS,
        )

    BaseVisualizationTestInit, BaseVisualizationTest = factory()


class TestModelInit(BaseVisualizationTest.BaseVisualizationTestInit):
    pass


class TestModel(BaseVisualizationTest.BaseVisualizationTest):
    def _test_set_model(self):
        self.assertEqual(self.model.static_data, self.static_data)

    def _test_call(self, results, variables):
        variable_name = self.model.cfg['VARIABLE_NAME']
        self.assertEqual(self.model.ax._children[0]._text, TEST_PARAMS['VARIABLES'][variable_name])


if __name__ == '__main__':
    unittest.main()
