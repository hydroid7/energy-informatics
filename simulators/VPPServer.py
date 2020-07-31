from typing import List

from interfaces.informationObjects import TimeIntervalPowerRequirement
from interfaces.interfaces import AbstractVPPServer


class VPPServer(AbstractVPPServer):
    def set_market_energy_requirement(self, requirements: TimeIntervalPowerRequirement):
        pass

    def get_pv_setpoints(self) -> List:
        pass