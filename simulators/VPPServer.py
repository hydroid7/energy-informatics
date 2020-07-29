from typing import List

from interfaces.informationObjects import TimeIntervalPowerRequirement
from interfaces.interfaces import AbstractVPPServer


class VPPServer(AbstractVPPServer):
    def set_market_energy_requirement(self, requirements: TimeIntervalPowerRequirement):
        pass

    def get_pv_setpoints(self) -> List:
        pass

    def init(self, sid, **sim_params):
        pass

    def create(self, num, model, **model_params):
        pass

    def step(self, time, inputs):
        pass

    def get_data(self, outputs) -> dict:
        pass
