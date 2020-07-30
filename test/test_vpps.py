#Realized by Basma and Pryanka

import unittest
from vpps import vppServer

vpps = vppServer()

class TestVPPS(unittest.TestCase):

    def test_set_market_energy_requirement(self):
        #testing the sum of p_feedin_i
        # it will return the sum
        self.assertEqual(vpps.aggregated_current([2, 5, 3, 7]), 17)
        #testing when P_target - P_feedin > 0
        #it will retun the pv_count
        self.assertEqual(vpps.switch_pvSystem(90, 30), 3)
        #testing wen P_target - P_feedin < 0
        #it will return a sorted list
        self.assertEqual(vpps.sort_pvSystem([4, 2, 1, 6]), [1, 2, 4, 6])
        # testing when the diff < 0
        # it will delete the pv Systen with the highest current feed in
        self.assertEqual(vpps.switch_off_pvSystem([1, 2, 4, 6]), [1, 2, 4])
        # it will update the difference
        self.assertEqual(vpps.update_difference(90, [1, 2, 4]), 90/7)

    # logic remains the same for the vpps and the pvc
    def test_adjust_feedin_power(self):
        #testing the inactive status of PV so feed in power is equal to 0
        self.assertEqual(vpps.adjust_feedin_power(0, 10), 0)
        #testing the active status of PV so the feed in power is equal to P_set
        self.assertEqual(vpps.adjust_feedin_power(1, 10), 10)


if __name__ == '__main__':
    unittest.main()
