from interfaces.informationObjects import GridPowerReading
from interfaces.interfaces import AbstractPVController


class PVController(AbstractPVController):
    def set_grid_voltage(self):
        pass

    def set_operation_state(self, feed_in=True) -> None:
        pass

    def get_real_feed_in(self) -> GridPowerReading:
        pass

    def init(self, sid, **sim_params):
        pass

    def create(self, num, model, **model_params):
        pass

    def step(self, time, inputs):
        pass

    def get_data(self, outputs) -> dict:
        pass

    def adjust_real_power_output(self) -> None:
        pass
