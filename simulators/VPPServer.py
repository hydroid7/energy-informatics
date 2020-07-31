from typing import List

from interfaces.informationObjects import TimeIntervalPowerRequirement
from interfaces.interfaces import AbstractVPPServer

PEAK_PV_POWER = 10000  # in W


class VPPServer(AbstractVPPServer):

    def __init__(self, energy_requirements: TimeIntervalPowerRequirement):
        self._energy_requirements = energy_requirements

    def set_market_energy_requirement(self, requirements: TimeIntervalPowerRequirement):
        self._energy_requirements = requirements

    def get_pv_setpoints(self, pv_feed_in: List) -> List:
        pass
