__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from unittest import TestCase, main
from simulators.VPPServer import VPPServer
from interfaces.informationObjects import MarketPowerRequirement, PowerFeedIn

vpp_server = VPPServer()


class VPPServerTestCase(TestCase):

    def test_enable_pv_systems_when_requirement_is_large(self):
        e_requirements = MarketPowerRequirement(30_000)
        vpp_server.set_market_energy_requirement(e_requirements)
        feed_in = PowerFeedIn([200, 500, 400, 600, 0, 0])

        setpoints = vpp_server.get_pv_setpoints(feed_in)
        self.assertListEqual(setpoints.pv_plants, [10_000, 0, 0, 0, 0, 0])

    def test_disable_pv_systems_when_requirement_is_low(self):
        e_requirements = MarketPowerRequirement(2_000)
        vpp_server.set_market_energy_requirement(e_requirements)
        feed_in = PowerFeedIn([200, 500, 400, 600, 100, 0])
        setpoints = vpp_server.get_pv_setpoints(feed_in)
        self.assertListEqual(setpoints.pv_plants, [0, 0, 0, 0, 100, 0])


if __name__ == '__main__':
    main()
