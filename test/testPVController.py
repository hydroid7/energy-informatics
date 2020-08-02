import unittest
from simulators.PVController import PVController

pvc = PVController()


class TestPVC(unittest.TestCase):

    def test_adjust_real_power_output(self):
        #testing first condition: U_I=260 > U_nom * 1.1, expected output P_set = 0
        self.assertEqual(pvc.adjust_real_power_output(260.0), 0)
        #testing second condition: U_I=240 < U_nom * 1.05, expected output P_set = P_peak = 10
        self.assertEqual(pvc.adjust_real_power_output(240.0), 10000)
        #testing third condition:U_nom * 1.05 < U_I=250 < U_nom * 1.1, expected output P_set follows the linear curve
        self.assertEqual(pvc.adjust_real_power_output(250.0),  10000 * (22 - 20 * (250.0/230.0)))

    def test_adjust_feedin_power(self):
        #testing the inactive status of PV so feed in power is equal to 0
        self.assertEqual(pvc.adjust_feedin_power(0, 10), 0)
        #testing the active status of PV so the feed in power is equal to P_set
        self.assertEqual(pvc.adjust_feedin_power(1, 10), 10)

    def test_active_operation_state(self):
        #if state is active so pv status is set to 1
        self.assertEqual(pvc._active_operation_state(True), 1)
        #if state is inactive so pv status is set to 0
        self.assertEqual(pvc._active_operation_state(False), 0)


if __name__ == '__main__':
    unittest.main()
