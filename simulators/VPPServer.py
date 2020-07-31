__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from math import ceil
from interfaces.informationObjects import MarketPowerRequirement, PowerFeedIn
from interfaces.interfaces import AbstractVPPServer

PEAK_PV_POWER = 10000  # in W


class VPPServer(AbstractVPPServer):

    def __init__(self):
        self._energy_requirements = MarketPowerRequirement(0)

    def set_market_energy_requirement(self, requirements: MarketPowerRequirement):
        self._energy_requirements = requirements

    def get_pv_setpoints(self, pv_feed_in: PowerFeedIn) -> PowerFeedIn:
        diff = self._calculate_diff(pv_feed_in)
        if diff < 0:
            return self._disable_pv_systems(pv_feed_in)
        else:
            return self._enable_pv_systems(diff, pv_feed_in)

    def _calculate_diff(self, pv_feed_in):
        current_feed_in = pv_feed_in.total_feed_in()
        target = self._energy_requirements.power_requirement_per_minute()
        return target - current_feed_in

    def _disable_pv_systems(self, pv_feed_in: PowerFeedIn):
        current_feed_in = pv_feed_in
        while self._calculate_diff(current_feed_in) < 0:
            index = current_feed_in.index_max_feeder()
            new_feed_in_list = current_feed_in.pv_plants
            new_feed_in_list[index] = 0
            current_feed_in = PowerFeedIn(new_feed_in_list)
        return current_feed_in

    def _enable_pv_systems(self, diff, pv_feed_in: PowerFeedIn) -> PowerFeedIn:
        pv_count = ceil(diff/PEAK_PV_POWER)
        enabled_pv_systems = [PEAK_PV_POWER] * pv_count
        disabled_pv_systems = [0] * (len(pv_feed_in.pv_plants) - pv_count)
        return PowerFeedIn(enabled_pv_systems + disabled_pv_systems)
