import unittest
from simulators.PVController import PVController

pvc = PVController()


class TestPVC(unittest.TestCase):

    def test_adjust_real_power_output(self):
        self.assertEqual(pvc.set_grid_voltage(), 120)
